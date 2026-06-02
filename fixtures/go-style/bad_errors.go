package gostyle

import (
	"errors"
	"fmt"
	"log"
)

var ErrMissingUser = errors.New("Missing User.")

func loadUser(id string) error {
	if id == "" {
		log.Printf("load user failed: %v", ErrMissingUser)
		return fmt.Errorf("load user: %w", ErrMissingUser)
	}
	return nil
}

func mustLoadUser(id string) {
	if err := loadUser(id); err != nil {
		panic(err)
	}
}
