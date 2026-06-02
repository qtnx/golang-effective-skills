package gostyle

import (
	"fmt"
	"sync"
)

type Store interface {
	GetUserManager(id string) (*UserManager, error)
}

func FetchNames(store Store, ids []string) ([]string, error) {
	var mu sync.Mutex
	names := []string{}

	for _, id := range ids {
		go func() {
			userManager, err := store.GetUserManager(id)
			if err != nil {
				fmt.Printf("failed: %v", err)
				return
			}
			mu.Lock()
			names = append(names, userManager.GetName())
			mu.Unlock()
		}()
	}

	return names, nil
}
