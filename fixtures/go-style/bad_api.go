package gostyle

type UserManager struct {
	name string
}

func NewUserManager(name string) *UserManager {
	return &UserManager{name: name}
}

func (userManager *UserManager) GetName() string {
	return userManager.name
}

type UserManagerInterface interface {
	GetName() string
	Save() error
	Delete() error
	Archive() error
}

func ProcessUserManager(userManager UserManagerInterface) error {
	return userManager.Save()
}
