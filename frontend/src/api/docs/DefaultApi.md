# DefaultApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**createComment**](#createcomment) | **POST** /books/{book_id}/comments | Create Comment|
|[**getBook**](#getbook) | **GET** /books/{book_id}/content | Get Book|
|[**getBookComments**](#getbookcomments) | **GET** /books/{book_id}/comments | Get Book Comments|
|[**getBooks**](#getbooks) | **GET** /books | Get Books|
|[**loginUser**](#loginuser) | **POST** /login | Login User|
|[**registerUser**](#registeruser) | **POST** /register | Register User|

# **createComment**
> any createComment(commentCreate)


### Example

```typescript
import {
    DefaultApi,
    Configuration,
    CommentCreate
} from 'toto-app-api-client';

const configuration = new Configuration();
const apiInstance = new DefaultApi(configuration);

let bookId: number; // (default to undefined)
let commentCreate: CommentCreate; //

const { status, data } = await apiInstance.createComment(
    bookId,
    commentCreate
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **commentCreate** | **CommentCreate**|  | |
| **bookId** | [**number**] |  | defaults to undefined|


### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getBook**
> string getBook()


### Example

```typescript
import {
    DefaultApi,
    Configuration
} from 'toto-app-api-client';

const configuration = new Configuration();
const apiInstance = new DefaultApi(configuration);

let bookId: number; // (default to undefined)

const { status, data } = await apiInstance.getBook(
    bookId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bookId** | [**number**] |  | defaults to undefined|


### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getBookComments**
> any getBookComments()


### Example

```typescript
import {
    DefaultApi,
    Configuration
} from 'toto-app-api-client';

const configuration = new Configuration();
const apiInstance = new DefaultApi(configuration);

let bookId: number; // (default to undefined)

const { status, data } = await apiInstance.getBookComments(
    bookId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bookId** | [**number**] |  | defaults to undefined|


### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getBooks**
> Array<Book> getBooks()


### Example

```typescript
import {
    DefaultApi,
    Configuration
} from 'toto-app-api-client';

const configuration = new Configuration();
const apiInstance = new DefaultApi(configuration);

const { status, data } = await apiInstance.getBooks();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**Array<Book>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loginUser**
> string loginUser(userLogin)

Authenticate user and return JWT token.

### Example

```typescript
import {
    DefaultApi,
    Configuration,
    UserLogin
} from 'toto-app-api-client';

const configuration = new Configuration();
const apiInstance = new DefaultApi(configuration);

let userLogin: UserLogin; //

const { status, data } = await apiInstance.loginUser(
    userLogin
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **userLogin** | **UserLogin**|  | |


### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registerUser**
> any registerUser(userCreate)

Register a new user with username and password.

### Example

```typescript
import {
    DefaultApi,
    Configuration,
    UserCreate
} from 'toto-app-api-client';

const configuration = new Configuration();
const apiInstance = new DefaultApi(configuration);

let userCreate: UserCreate; //

const { status, data } = await apiInstance.registerUser(
    userCreate
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **userCreate** | **UserCreate**|  | |


### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

