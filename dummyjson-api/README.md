# DummyJSON Independent API Testing

## Overview

Manual API testing project performed on the DummyJSON REST API using **Postman**.

I independently explored the API documentation, selected test scenarios, executed positive and negative tests, compared expected vs. actual behavior, and verified simulated persistence behavior.

**Environment:** Windows 11 | Postman  
**Scope:** Authentication, Products, Recipes, Posts, Comments, Todos

---

## 1. API Reconnaissance

| Test | Actual Result | Status |
|---|---|---|
| `GET /auth/me` | Authenticated user information returned — `200` | PASS |
| `GET /products?sortBy=title&order=asc` | 30 products returned in ascending title order — `200` | PASS |
| `GET /products/categories` | 24 categories returned with name, slug and URL — `200` | PASS |

This stage was used to understand the API resources, JSON responses, authentication behavior, and documentation before formal testing.

---

## 2. Positive & Negative Testing

| Test | Expected | Actual | Status |
|---|---|---|---|
| Valid login | Authentication succeeds | `200`, user information returned | PASS |
| Invalid login | Authentication rejected | `400`, invalid credentials | PASS |
| `GET /products/10` | Existing product returned | `200`, product 10 returned | PASS |
| Nonexistent product ID | Product not returned | `404`, product not found | PASS |

The invalid-login test also reinforced that a negative test passes when invalid input is correctly rejected; the exact HTTP status should be evaluated against the API specification rather than assumed.

---

## 3. Create & Persistence Testing

**Create recipe**

`POST /recipes/add`

Request body:

```json
{
  "name": "Chicken Healthy Fried"
}
```

Result: `201 Created`, returning recipe ID `51`.

**Persistence check**

`GET /recipes/51` → `404 Not Found`

The POST successfully simulated creation, but the follow-up GET confirmed that the new resource was not permanently stored, consistent with DummyJSON's documented simulated behavior.

**Status:** PASS

---

## 4. Update & Delete Testing

### Update

`PUT /posts/1`

Changed title to:

> I think I should shift to the moon

The PUT returned `200` with the modified title.

A follow-up `GET /posts/1` returned the original title:

> His mother had always taught him

This confirmed that the simulated update did not persist.

### Delete

`DELETE /comments/1` → `200`

The response included:

- `isDeleted: true`
- `deletedOn` timestamp

This was treated as confirmation of the simulated delete response, not proof of permanent deletion.

**Status:** PASS

---

## 5. Independent Todos Testing

For the final exercise, I independently selected and executed a small functional test scope for the Todos API based on its documentation.

| Test | Actual Result | Status |
|---|---|---|
| Default Todos retrieval | 30 Todos — `200` | PASS |
| `limit=254` | 254 Todos — `200` | PASS |
| `limit=260` | 254 available Todos returned — `200` | PASS |
| Existing Todo ID | Correct Todo returned — `200` | PASS |
| Random Todo | Existing Todo returned — `200` | PASS |
| Nonexistent Todo ID | `404 Not Found` | PASS |
| Field selection | Only selected information returned | PASS |
| Sort by `userId` | Ascending & descending worked | PASS |
| Sort by Todo text | Ascending & descending worked | PASS |
| Sort by ID | Ascending & descending worked | PASS |
| Valid Todo creation | Simulated resource returned — `201` | PASS |
| Missing required POST data | `400`, `userId` required | PASS |
| GET newly created Todo | Resource not found as expected | PASS |

The final persistence check was consistent with DummyJSON's documented simulated creation behavior.

---

## Key Skills Demonstrated

- Reading unfamiliar API documentation
- Manual API testing with Postman
- GET, POST, PUT and DELETE requests
- Positive and negative testing
- HTTP status-code interpretation
- JSON request and response inspection
- Query parameters, sorting and field selection
- Input validation testing
- Create/update/delete behavior
- Persistence verification
- Expected vs. actual result analysis

## Conclusion

The **tested functionality** behaved consistently with expected or documented behavior, and no defect was identified in the scenarios covered.

This was a targeted manual API test and does not claim complete coverage of the DummyJSON API.