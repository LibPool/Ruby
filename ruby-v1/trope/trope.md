# trope

**Tag**: web, cli, testing, networking, tooling, filesystem

## 简介

# Trope

**[Documentation][docs] - [Gem][gems] - [Source][source]**

Prototyping language that transcompiles into pure Ruby code.

1. Build your concept in Trope.
2. Write specs.
3. Transcompile into Ruby.
4. Destroy Trope files.
5. Red, green, refactor.

## Install

> NOTE:  Trope is not released yet, the gem is just a placeholder.

### Bundler: `gem 'trope'`

### RubyGems: `gem install trope`

## Example

Create `library.trope`:

```ruby
object Book
  attr name <String> -!wd 'Unnamed book'
  attr isbn <Integer> -w
  attr library <Library> -w do
    before write { @library.books.delete(self) unless @library.nil? }
    after  write { @library.books.push(self) unless @library.books.include?(self) }
  end
end

object Library
  attr books <Array> -d Array.new
  meth add_book do |attributes_or_book <Hash, Book>|
    book = attributes_or_book.is_a?(Book) ? attributes_or_book : Book.new(attributes_or_book)
    book.library = self
    
    @books << book
  end
end
```

Now generate the Ruby code:

```sh
$ trope compile libary.trope
```

Those 15 lines will be transcompiled into the following pure Ruby code in `library.rb`:

```ruby
class Book
  class Error < RuntimeError; end
  
  class InvalidAttributesError < Error
    def to_s
      'attributes must be a Hash or respond to #to_h'
    end
  end
  
  class MissingAttributeError < Error
    def initialize(attr_name, attr_class)
      @name, @class = attr_name.to_s, attr_class.to_s
    end
    
    def to_s
      "attribute '#@name' does not exist for #@class"
    end
  end
  
  class MissingNameError < Error
    def to_s
      'name cannot be nil'
    end
  end
  
  class InvalidNameError < Error
    def to_s
      'name must be an instance of String or respond to :to_s'
    end
  end
  
  class InvalidIsbnError < Error
    def to_s
      'isbn must be an instance of Integer or respond to :to_i'
    end
  end
  
  class MissingLibraryError < Error
    def to_s
      'library cannot be nil'
    end
  end
  
  class InvalidLibraryError < Error
    def to_s
      'library must be an instance of Library'
    end
  end
  
  attr_reader *(@@_attributes = [:name, :isbn, :library])
  
  def initialize(attributes={})
    raise InvalidAttributesError unless attributes.is_a?(Hash) || attributes.respond_to?(:to_h)
    attributes = attributes.to_h unless attributes.is_a?(Hash)
    
    raise MissingNameError if attributes.has_key?(:name) && attributes[:name].nil?
    attributes[:name] = 'Unnamed book' unless attributes.has_key?(:name)
    
    attributes.each do |name, value|
      raise MissingAttributeError.new(name, self.class) unless @@_attributes.include?(name.to_sym)
      
      setter_method = "#{name}="
      setter_method = "_#{setter_method}" unless self.class.method_defined?(setter_method)
      
      send(setter_method, value)
    end
  end
  
  def name=(value)
    raise MissingNameError if value.nil?
    raise InvalidNameError unless value.is_a?(String) || value.respond_to?(:to_s)
    value = value.to_i unless value.is_a?(Integer)
    
    @name = value
  end
  
  def isbn=(value)
    raise InvalidIsbnError unless value.is_a?(Integer) || value.respond_to?(:to_i)
    value = value.to_i unless value.is_a?(Integer)
    
    @isbn = value
  end
  
  def library=(value)
    raise InvalidLibraryError unless value.is_a?(Library) || value.nil?
    
    @library.books.delete(self) unless @library.nil?
    
    @library = value
    
    @library.books.push(self) unless @library.books.include?(self)
    
    @library
  end
end

class Library
  class Error < RuntimeError; end
  
  class InvalidAttributesError < Error
    def to_s
      'attributes must be an instance of Hash or respond to #to_h'
    end
  end
  
  class MissingAttributeError < Error
    def initialize(attr_name, attr_class)
      @name, @class = attr_name.to_s, attr_class.to_s
    end
    
    def to_s
      "attribute '#@name' does not exist for #@class"
    end
  end
  
  class InvalidBooksError < Error
    def to_s
      'books must be an instance of Array or respond to #to_a'
    end
  end
  
  attr_reader *(@@_attributes = [:books])
  
  def initialize(attributes={})
    raise InvalidAttributesError unless attributes.is_a?(Hash) || attributes.respond_to?(:to_h)
    attributes = attributes.to_h unless attributes.is_a?(Hash)
    
    attributes[:books] = Array.new unless attributes.has_key?(:books)
    
    attributes.each do |name, value|
      raise MissingAttributeError.new(name, self.class) unless @@_attributes.include?(name.to_sym)
      
      setter_method = "#{name}="
      setter_method = "_#{setter_method}" unless self.class.method_defined?(setter_method)
      
      send(setter_method, value)
    end
  end
  
  def add_book(attributes_or_book={})
    raise InvalidAttributesError unless attributes_or_book.is_a?(Hash) || attributes_or_book.respond_to?(:to_h) || attributes_or_book.is_a?(Book)
    attributes_or_book = attributes_or_book.to_h unless attributes_or_book.is_a?(Hash) || attributes_or_book.is_a?(Book)
    
    book = attributes_or_book.is_a?(Book) ? attributes_or_book : Book.new(attributes_or_book)
    book.library = self
    
    @books << book
  end
  
  protected
  
  def _books=(value)
    raise InvalidBooksError unless value.is_a?(Array) || value.respond_to?(:to_a)
    value = value.to_a unless value.is_a?(Array)
    
    @books = value
  end
end
```

Using the transcompiled Ruby code will produce the expected results:

```ruby
p library = Library.new                     # => #<Library:0x007fc55c0ce418 @books=[]>
p library.add_book name: 'Book 1', isbn: 1  # => [#<Book:0x007fc55c0cde78 @name=0, @isbn=1, @library=#<Library:0x007fc55c0ce418 @books=[...]>>]
p library                                   # => #<Library:0x007fc55c0ce418 @books=[#<Book:0x007fc55c0cde78 @name=0, @isbn=1, @library=#<Library:0x007fc55c0ce418 ...>>]>
p library.books.first                       # => #<Book:0x007fc55c0cde78 @name=0, @isbn=1, @library=#<Library:0x007fc55c0ce418 @books=[#<Book:0x007fc55c0cde78 ...>]>>
p library.books.first.isbn = nil            # => nil
p library.books.first.name = nil            # => Book::MissingNameError: name cannot be nil
p library.books.first.library = nil         # => Book::MissingLibraryError: library cannot be nil
p library.books.first.isbn = ['array']      # => Book::InvalidIsbnError: isbn must be an instance of Integer or respond to :to_i
p library = Library.new(books: 123)         # => Library::InvalidBooksError: books must be an instance of Array or respond to #to_a
```

### Breakdown

```ruby
object Book
  attr name <String> -!wd 'Unnamed book'
end
```

This says that I have an object `Book` that has an attribute `name` (`attr name`) that 
must either be an instance/subclass of `String` or be able to convert to an instance of 
`String` using `#to_s` (`<String>`). It is a required attribute that can never be set to nil (`!`), has a writer method (`w`),
and defaults to 'Unnamed book'.

The minus sign (`-`) indicates a 'switch' or 'option', must like most *nix command line 
programs. The example could also have been written like so:

```ruby
object Book
  attr name <String> -! -w -d 'Unnamed book'
end
```

The above examples will transcompile into the following:

```ruby
class Book
  class Error < RuntimeError; end
  
  class InvalidAttributesError < Error
    def to_s
      'attributes must be a Hash or respond to #to_h'
    end
  end
  
  class MissingAttributeError < Error
    def initialize(attr_name, attr_class)
      @name, @class = attr_name.to_s, attr_class.to_s
    end
    
    def to_s
      "attribute '#@name' does not exist for #@class"
    end
  end
  
  class MissingNameError < Error
    def to_s
      'name cannot be nil'
    end
  end
  
  class InvalidNameError < Error
    def to_s
      'name must be an instance of String or respond to :to_s'
    end
  end
  
  attr_reader *(@@_attributes = [:name])
  @@_required_attributes = [:name]
  
  def initialize(attributes={})
    raise InvalidAttributesError unless attributes.is_a?(Hash) || attributes.respond_to?(:to_h)
    attributes = attributes.to_h unless attributes.is_a?(Hash)
    
    raise MissingNameError if attributes.has_key?(:name) && attributes[:name].nil?
    
    attributes[:name] = 'Unnamed book' unless attributes.has_key?(:name)
    
    attributes.each do |name, value|
      raise MissingAttributeError.new(name, self.class) unless @@_attributes.include?(name.to_sym)
      
      setter_method = "#{name}="
      setter_method = "_#{setter_method}" unless self.class.method_defined?(setter_method)
      
      send(setter_method, value)
    end
  end
  
  def name=(value)
    raise MissingNameError if value.nil?
    raise InvalidNameError unless value.is_a?(String) || value.respond_to?(:to_s)
    value = value.to_i unless value.is_a?(Integer)
    
    @name = value
  end
end
```

## Contributing

* Check out the latest master to make sure the feature hasn't been implemented or the bug hasn't been fixed yet
* Check out the issue tracker to make sure someone already hasn't requested it and/or contributed it
* Fork the project
* Start a feature/bugfix branch
* Commit and push until you are happy with your contribution
* Make sure to add tests for it. This is important so I don't break it in a future version unintentionally.
* Please try not to mess with the Rakefile, VERSION, or Gemfile. If you want to have your own version, or is otherwise necessary, that is fine, but please isolate to its own commit so I can cherry-pick around it.

## Copyright

Copyright © 2012 Ryan Scott Lewis <ryan@rynet.us>.

The MIT License (MIT) - See LICENSE for further details.

[docs]: http://rubydoc.info/gems/trope/frames
[gems]: https://rubygems.org/gems/trope
[source]: https://github.com/RyanScottLewis/trope

## 官网

- 主页: http://github.com/RyanScottLewis/trope
- RubyGems: https://rubygems.org/gems/trope

## 历史版本号

- 0.0.0 (2012-12-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/trope
- gem 安装: `gem install trope`
- Bundler: `gem "trope"`
- 最新版本: 0.0.0
- 最新版归档: https://rubygems.org/downloads/trope-0.0.0.gem
- 版本锁定: `gem "trope", "~> 0.0.0"`
- 中央仓库: https://rubygems.org/
