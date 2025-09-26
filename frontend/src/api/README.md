## toto-app-api-client@1.0.0

This generator creates TypeScript/JavaScript client that utilizes [axios](https://github.com/axios/axios). The generated Node module can be used in the following environments:

Environment

- Node.js
- Webpack
- Browserify

Language level

- ES5 - you must have a Promises/A+ library installed
- ES6

Module system

- CommonJS
- ES6 module system

It can be used in both TypeScript and JavaScript. In TypeScript, the definition will be automatically resolved via `package.json`. ([Reference](https://www.typescriptlang.org/docs/handbook/declaration-files/consumption.html))

### Documentation for API Endpoints

All URIs are relative to _<http://localhost>_

| Class        | Method                                                    | HTTP request                       | Description       |
| ------------ | --------------------------------------------------------- | ---------------------------------- | ----------------- |
| _DefaultApi_ | [**createComment**](docs/DefaultApi.md#createcomment)     | **POST** /books/{book_id}/comments | Create Comment    |
| _DefaultApi_ | [**getBook**](docs/DefaultApi.md#getbook)                 | **GET** /books/{book_id}/content   | Get Book          |
| _DefaultApi_ | [**getBookComments**](docs/DefaultApi.md#getbookcomments) | **GET** /books/{book_id}/comments  | Get Book Comments |
| _DefaultApi_ | [**getBooks**](docs/DefaultApi.md#getbooks)               | **GET** /books                     | Get Books         |
| _DefaultApi_ | [**loginUser**](docs/DefaultApi.md#loginuser)             | **POST** /login                    | Login User        |
| _DefaultApi_ | [**registerUser**](docs/DefaultApi.md#registeruser)       | **POST** /register                 | Register User     |

### Documentation For Models

- [Book](docs/Book.md)
- [CommentCreate](docs/CommentCreate.md)
- [HTTPValidationError](docs/HTTPValidationError.md)
- [UserCreate](docs/UserCreate.md)
- [UserLogin](docs/UserLogin.md)
- [ValidationError](docs/ValidationError.md)
- [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)

<a id="documentation-for-authorization"></a>

## Documentation For Authorization

Endpoints do not require authorization.
