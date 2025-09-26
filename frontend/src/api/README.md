## toto-app-api-client@1.0.0

This generator creates TypeScript/JavaScript client that utilizes [axios](https://github.com/axios/axios). The generated Node module can be used in the following environments:

Environment
* Node.js
* Webpack
* Browserify

Language level
* ES5 - you must have a Promises/A+ library installed
* ES6

Module system
* CommonJS
* ES6 module system

It can be used in both TypeScript and JavaScript. In TypeScript, the definition will be automatically resolved via `package.json`. ([Reference](https://www.typescriptlang.org/docs/handbook/declaration-files/consumption.html))

### Building

To build and compile the typescript sources to javascript use:
```
npm install
npm run build
```

### Publishing

First build the package then run `npm publish`

### Consuming

navigate to the folder of your consuming project and run one of the following commands.

_published:_

```
npm install toto-app-api-client@1.0.0 --save
```

_unPublished (not recommended):_

```
npm install PATH_TO_GENERATED_PACKAGE --save
```

### Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**createComment**](docs/DefaultApi.md#createcomment) | **POST** /books/{book_id}/comments | Create Comment
*DefaultApi* | [**getBook**](docs/DefaultApi.md#getbook) | **GET** /books/{book_id}/content | Get Book
*DefaultApi* | [**getBookComments**](docs/DefaultApi.md#getbookcomments) | **GET** /books/{book_id}/comments | Get Book Comments
*DefaultApi* | [**getBooks**](docs/DefaultApi.md#getbooks) | **GET** /books | Get Books
*DefaultApi* | [**getCurrentUser**](docs/DefaultApi.md#getcurrentuser) | **GET** /me | Get Current User
*DefaultApi* | [**loginUser**](docs/DefaultApi.md#loginuser) | **POST** /login | Login User
*DefaultApi* | [**registerUser**](docs/DefaultApi.md#registeruser) | **POST** /register | Register User


### Documentation For Models

 - [Book](docs/Book.md)
 - [CommentCreate](docs/CommentCreate.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [User](docs/User.md)
 - [UserCreate](docs/UserCreate.md)
 - [UserLogin](docs/UserLogin.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.

