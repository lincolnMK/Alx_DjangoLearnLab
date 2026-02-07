# API Views — advanced-api-project

This document describes how each view in the `api` app is configured, how it is intended to operate, and any custom hooks or settings that modify default behavior.

Files referenced:
- Views: [api/views.py](api/views.py)
- URLs: [api/urls.py](api/urls.py)
- Serializers: [api/serializers.py](api/serializers.py)
- Project settings: [advanced_api_project/settings.py](advanced_api_project/settings.py)

## Overview

The `api` app exposes REST endpoints for `Book` and `Author` resources using Django REST Framework generic views. Permissions are applied via DRF permission classes defined on each view class.

## Views

- **BookList** (`books/`)
  - Class: `generics.ListCreateAPIView`
  - Endpoint: `GET /books/` (list), `POST /books/` (create)
  - Queryset: `Book.objects.all()`
  - Serializer: `BookSerializer`
  - Permissions: `IsAuthenticatedOrReadOnly` — unauthenticated users can view lists; creating requires authentication.

- **BookDetail** (`books/<int:pk>/`)
  - Class: `generics.RetrieveUpdateDestroyAPIView`
  - Endpoint: `GET /books/<pk>/`, `PUT/PATCH /books/<pk>/`, `DELETE /books/<pk>/`
  - Queryset: `Book.objects.all()`
  - Serializer: `BookSerializer`
  - Permissions: `IsAuthenticatedOrReadOnly` — read access for unauthenticated, modifications require authentication.

- **AuthorList** (`authors/`)
  - Class: `generics.ListCreateAPIView`
  - Endpoint: `GET /authors/`, `POST /authors/`
  - Queryset: `Author.objects.all()`
  - Serializer: `AuthorSerializer` (includes nested `books` read-only field)
  - Permissions: `IsAuthenticatedOrReadOnly`.

- **AuthorDetail** (`authors/<int:pk>/`)
  - Class: `generics.RetrieveUpdateDestroyAPIView`
  - Endpoint: `GET /authors/<pk>/`, `PUT/PATCH /authors/<pk>/`, `DELETE /authors/<pk>/`
  - Queryset: `Author.objects.all()`
  - Serializer: `AuthorSerializer`
  - Permissions: `IsAuthenticatedOrReadOnly`.

- **AuthorBooks** (`authors/<int:author_id>/books/`)
  - Class: `generics.ListAPIView`
  - Endpoint: `GET /authors/<author_id>/books/` — lists books for the given author.
  - Serializer: `BookSerializer`
  - Custom hook: overrides `get_queryset()` to read `author_id` from `kwargs` and return `Book.objects.filter(author__id=author_id)`.
  - Note: URL must provide `author_id` (see [api/urls.py](api/urls.py)). If `author_id` is missing the view will raise a `KeyError`.

- **CreateBook** ('books/create/')
  - Class: `generics.CreateAPIView`
  - Permission: `IsAuthenticated` (requires authentication to create)
  - Queryset: `Book.objects.all()`
  - Serializer: `BookSerializer`
  - Note: this view class exists in `api/views.py` but is not currently referenced in `api/urls.py`.

- **UpdateBook** ('books/<int:pk>/update/')
  - Class: `generics.UpdateAPIView`
  - Permission: `IsAuthenticated`
  - Queryset: `Book.objects.all()`
  - Serializer: `BookSerializer`
  - Note: also defined but not wired into URLs by default.

## Serializers and model-level hooks affecting views

- `BookSerializer` ([api/serializers.py](api/serializers.py))
  - Uses `ModelSerializer` with `fields='__all__'`.
  - Implements `validate_publication_year` to reject future publication years. This validation runs on create and update requests and will return HTTP 400 for invalid input.

- `AuthorSerializer` ([api/serializers.py](api/serializers.py))
  - Includes a nested, read-only `books` field serialized via `BookSerializer`. When retrieving authors (list or detail), the serialized response includes the author's books.

## Permissions and authentication

- Views use DRF permission classes declared on the view classes (e.g. `IsAuthenticatedOrReadOnly`, `IsAuthenticated`). These rely on DRF authentication configuration in project settings. 