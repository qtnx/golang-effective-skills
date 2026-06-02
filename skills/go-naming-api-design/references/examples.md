# Examples

Use these as calibration snippets before proposing API or naming changes.

## Package Stutter

```go
package user

type UserManager struct{}
func NewUserManager() *UserManager
```

Prefer names that read well at the call site:

```go
package user

type Manager struct{}
func NewManager() *Manager
```

## Getter Names

```go
func (u *User) GetName() string
```

```go
func (u *User) Name() string
```

## Consumer-Owned Interfaces

```go
type UserManagerInterface interface {
	Save() error
	Delete() error
	Archive() error
}
```

Prefer the narrow interface required by the consumer:

```go
type userSaver interface {
	Save() error
}
```

## Receiver Names

```go
func (userManager *Manager) Save() error
```

```go
func (m *Manager) Save() error
```
