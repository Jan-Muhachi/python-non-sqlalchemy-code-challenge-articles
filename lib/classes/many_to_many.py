class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Author name must be a non-empty string")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles[:]  # Return a copy of the list

    def magazines(self):
        return list(set([article.magazine for article in self._articles]))

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine argument must be a Magazine instance")
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)
        magazine.add_article(self, title)
        return new_article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set([article.magazine.category for article in self._articles]))


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise ValueError("Magazine name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Magazine category must be a non-empty string")
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or len(new_name) < 2 or len(new_name) > 16:
            raise ValueError("Magazine name must be a string between 2 and 16 characters")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Magazine category must be a non-empty string")
        self._category = new_category

    def articles(self):
        return self._articles[:]  # Return a copy of the list

    def contributors(self):
        authors = [article.author for article in self._articles]
        return [author for author, count in collections.Counter(authors).items() if count > 2]

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        return self.contributors()

    def add_article(self, author, title):
        if not isinstance(author, Author):
            raise TypeError("Author argument must be an Author instance")
        new_article = Article(author, self, title)
        self._articles.append(new_article)


class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("Author argument must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine argument must be a Magazine instance")
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Article title must be a string between 5 and 50 characters")
        self._author = author
        self._magazine = magazine
        self._title = title

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise TypeError("Author argument must be an Author instance")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise TypeError("Magazine argument must be a Magazine instance")
        self._magazine = new_magazine
