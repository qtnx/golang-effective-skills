---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/golang.org/x/oauth2"
source_path: "sources/raw/external/pkg-go-dev-golang-org-x-oauth2-dc2f217817.html"
license_ref: ""
---

##   Documentation ¶

Package oauth2 provides support for making OAuth2 authorized and authenticated HTTP requests, as specified in RFC 6749 <https://rfc-editor.org/rfc/rfc6749.html>. It can additionally grant authorization with Bearer JWT.

- Variables
-  func GenerateVerifier() string
-  func NewClient(ctx context.Context, src TokenSource) *http.Client
-  func RegisterBrokenAuthHeaderProvider(tokenURL string)deprecated
-  func S256ChallengeFromVerifier(verifier string) string
-  type AuthCodeOption
-
-  func S256ChallengeOption(verifier string) AuthCodeOption
-  func SetAuthURLParam(key, value string) AuthCodeOption
-  func VerifierOption(verifier string) AuthCodeOption

-  type AuthStyle
-  type Config
-
-  func (c *Config) AuthCodeURL(state string, opts ...AuthCodeOption) string
-  func (c *Config) Client(ctx context.Context, t *Token) *http.Client
-  func (c *Config) DeviceAccessToken(ctx context.Context, da *DeviceAuthResponse, opts ...AuthCodeOption) (*Token, error)
-  func (c *Config) DeviceAuth(ctx context.Context, opts ...AuthCodeOption) (*DeviceAuthResponse, error)
-  func (c *Config) Exchange(ctx context.Context, code string, opts ...AuthCodeOption) (*Token, error)
-  func (c *Config) PasswordCredentialsToken(ctx context.Context, username, password string) (*Token, error)
-  func (c *Config) TokenSource(ctx context.Context, t *Token) TokenSource

-  type DeviceAuthResponse
-
-  func (d DeviceAuthResponse) MarshalJSON() ([]byte, error)
-  func (c *DeviceAuthResponse) UnmarshalJSON(data []byte) error

-  type Endpoint
-  type RetrieveError
-
-  func (r *RetrieveError) Error() string

-  type Token
-
-  func (t *Token) Extra(key string) any
-  func (t *Token) SetAuthHeader(r *http.Request)
-  func (t *Token) Type() string
-  func (t *Token) Valid() bool
-  func (t *Token) WithExtra(extra any) *Token

-  type TokenSource
-
-  func ReuseTokenSource(t *Token, src TokenSource) TokenSource
-  func ReuseTokenSourceWithExpiry(t *Token, src TokenSource, earlyExpiry time.Duration) TokenSource
-  func StaticTokenSource(t *Token) TokenSource

-  type Transport
-
-  func (t *Transport) CancelRequest(req *http.Request)deprecated
-  func (t *Transport) RoundTrip(req *http.Request) (*http.Response, error)

- Config
- Config (CustomHTTP)
- Config.DeviceAuth

This section is empty.

View Source <https://cs.opensource.google/go/x/oauth2/+/v0.36.0:oauth2.go;l=341>
```go
var HTTPClient internal.ContextKey
```

HTTPClient is the context key to use with context.WithValue to associate a *http.Client value with a context.
  View Source <https://cs.opensource.google/go/x/oauth2/+/v0.36.0:oauth2.go;l=27>
```go
var NoContext = context.TODO()
```

NoContext is the default context you should supply if not using your own context.Context.

Deprecated: Use context.Background or context.TODO instead.

```go
func GenerateVerifier() string
```

GenerateVerifier generates a PKCE code verifier with 32 octets of randomness. This follows recommendations in RFC 7636 <https://rfc-editor.org/rfc/rfc7636.html>.

A fresh verifier should be generated for each authorization. The resulting verifier should be passed to Config.AuthCodeURL or Config.DeviceAuth with S256ChallengeOption, and to Config.Exchange or Config.DeviceAccessToken with VerifierOption.

```go
func NewClient(ctx context.Context, src TokenSource) *http.Client
```

NewClient creates an *http.Client from a context.Context and TokenSource. The returned client is not valid beyond the lifetime of the context.

Note that if a custom *http.Client is provided via the context.Context it is used only for token acquisition and is not used to configure the *http.Client returned from NewClient.

As a special case, if src is nil, a non-OAuth2 client is returned using the provided context. This exists to support related OAuth2 packages.

```go
func RegisterBrokenAuthHeaderProvider(tokenURL string)
```

RegisterBrokenAuthHeaderProvider previously did something. It is now a no-op.

Deprecated: this function no longer does anything. Caller code that wants to avoid potential extra HTTP requests made during auto-probing of the provider's auth style should set Endpoint.AuthStyle.

```go
func S256ChallengeFromVerifier(verifier string) string
```

S256ChallengeFromVerifier returns a PKCE code challenge derived from verifier with method S256.

Prefer to use S256ChallengeOption where possible.

```go
type AuthCodeOption interface {
	// contains filtered or unexported methods
}
```

An AuthCodeOption is passed to Config.AuthCodeURL.

```go
var (
	// AccessTypeOnline and AccessTypeOffline are options passed
	// to the Options.AuthCodeURL method. They modify the
	// "access_type" field that gets sent in the URL returned by
	// AuthCodeURL.
	//
	// Online is the default if neither is specified. If your
	// application needs to refresh access tokens when the user
	// is not present at the browser, then use offline. This will
	// result in your application obtaining a refresh token the
	// first time your application exchanges an authorization
	// code for a user.
	AccessTypeOnline  AuthCodeOption = SetAuthURLParam("access_type", "online")
	AccessTypeOffline AuthCodeOption = SetAuthURLParam("access_type", "offline")

// ApprovalForce forces the users to view the consent dialog
	// and confirm the permissions request at the URL returned
	// from AuthCodeURL, even if they've already done so.
	ApprovalForce AuthCodeOption = SetAuthURLParam("prompt", "consent")
)
```

```go
func S256ChallengeOption(verifier string) AuthCodeOption
```

S256ChallengeOption derives a PKCE code challenge from the verifier with method S256. It should be passed to Config.AuthCodeURL or Config.DeviceAuth only.

```go
func SetAuthURLParam(key, value string) AuthCodeOption
```

SetAuthURLParam builds an AuthCodeOption which passes key/value parameters to a provider's authorization endpoint.

```go
func VerifierOption(verifier string) AuthCodeOption
```

VerifierOption returns a PKCE code verifier AuthCodeOption. It should only be passed to Config.Exchange or Config.DeviceAccessToken.

```go
type AuthStyle int
```

AuthStyle represents how requests for tokens are authenticated to the server.

```go
const (
	// AuthStyleAutoDetect means to auto-detect which authentication
	// style the provider wants by trying both ways and caching
	// the successful way for the future.
	AuthStyleAutoDetect AuthStyle = 0

// AuthStyleInParams sends the "client_id" and "client_secret"
	// in the POST body as application/x-www-form-urlencoded parameters.
	AuthStyleInParams AuthStyle = 1

// using HTTP Basic Authorization. This is an optional style
	// described in the OAuth2 RFC 6749 section 2.3.1 <https://rfc-editor.org/rfc/rfc6749.html#section-2.3.1>.
	AuthStyleInHeader AuthStyle = 2
)
```

```go
type Config struct {
	// ClientID is the application's ID.
	ClientID string

// ClientSecret is the application's secret.
	ClientSecret string

// Endpoint contains the authorization server's token endpoint
	// URLs. These are constants specific to each server and are
	// often available via site-specific packages, such as
	// google.Endpoint or github.Endpoint.
	Endpoint Endpoint

// RedirectURL is the URL to redirect users going through
	// the OAuth flow, after the resource owner's URLs.
	RedirectURL string

// Scopes specifies optional requested permissions.
	Scopes []string
	// contains filtered or unexported fields
}
```

Config describes a typical 3-legged OAuth2 flow, with both the client application information and the server's endpoint URLs. For the client credentials 2-legged OAuth2 flow, see the golang.org/x/oauth2/clientcredentials package.

```go

package main

import (
	"context"
	"fmt"
	"log"

"golang.org/x/oauth2"
)

func main() {
	ctx := context.Background()
	conf := &oauth2.Config{
		ClientID:     "YOUR_CLIENT_ID",
		ClientSecret: "YOUR_CLIENT_SECRET",
		Scopes:       []string{"SCOPE1", "SCOPE2"},
		Endpoint: oauth2.Endpoint{
			AuthURL:  "https://provider.com/o/oauth2/auth",
			TokenURL: "https://provider.com/o/oauth2/token",
		},
	}

// use PKCE to protect against CSRF attacks
	// https://www.ietf.org/archive/id/draft-ietf-oauth-security-topics-22.html#name-countermeasures-6
	verifier := oauth2.GenerateVerifier()

// Redirect user to consent page to ask for permission
	// for the scopes specified above.
	url := conf.AuthCodeURL("state", oauth2.AccessTypeOffline, oauth2.S256ChallengeOption(verifier))
	fmt.Printf("Visit the URL for the auth dialog: %v", url)

// Use the authorization code that is pushed to the redirect
	// URL. Exchange will do the handshake to retrieve the
	// initial access token. The HTTP Client returned by
	// conf.Client will refresh the token as necessary.
	var code string
	if _, err := fmt.Scan(&code); err != nil {
		log.Fatal(err)
	}
	tok, err := conf.Exchange(ctx, code, oauth2.VerifierOption(verifier))
	if err != nil {
		log.Fatal(err)
	}

client := conf.Client(ctx, tok)
	client.Get("...")
}

```

```go
Output:

```

Share Format Run

```go

package main

import (
	"context"
	"fmt"
	"log"
	"net/http"
	"time"

"golang.org/x/oauth2"
)

func main() {
	ctx := context.Background()

conf := &oauth2.Config{
		ClientID:     "YOUR_CLIENT_ID",
		ClientSecret: "YOUR_CLIENT_SECRET",
		Scopes:       []string{"SCOPE1", "SCOPE2"},
		Endpoint: oauth2.Endpoint{
			TokenURL: "https://provider.com/o/oauth2/token",
			AuthURL:  "https://provider.com/o/oauth2/auth",
		},
	}

// Redirect user to consent page to ask for permission
	// for the scopes specified above.
	url := conf.AuthCodeURL("state", oauth2.AccessTypeOffline)
	fmt.Printf("Visit the URL for the auth dialog: %v", url)

// Use the authorization code that is pushed to the redirect
	// URL. Exchange will do the handshake to retrieve the
	// initial access token. The HTTP Client returned by
	// conf.Client will refresh the token as necessary.
	var code string
	if _, err := fmt.Scan(&code); err != nil {
		log.Fatal(err)
	}

// Use the custom HTTP client when requesting a token.
	httpClient := &http.Client{Timeout: 2 * time.Second}
	ctx = context.WithValue(ctx, oauth2.HTTPClient, httpClient)

tok, err := conf.Exchange(ctx, code)
	if err != nil {
		log.Fatal(err)
	}

client := conf.Client(ctx, tok)
	_ = client
}

```

```go
Output:

```

Share Format Run

```go
func (c *Config) AuthCodeURL(state string, opts ...AuthCodeOption) string
```

AuthCodeURL returns a URL to OAuth 2.0 provider's consent page that asks for permissions for the required scopes explicitly.

State is an opaque value used by the client to maintain state between the request and callback. The authorization server includes this value when redirecting the user agent back to the client.

Opts may include AccessTypeOnline or AccessTypeOffline, as well as ApprovalForce.

To protect against CSRF attacks, opts should include a PKCE challenge (S256ChallengeOption). Not all servers support PKCE. An alternative is to generate a random state parameter and verify it after exchange. See https://datatracker.ietf.org/doc/html/rfc6749#section-10.12 <https://datatracker.ietf.org/doc/html/rfc6749#section-10.12> (predating PKCE), https://www.oauth.com/oauth2-servers/pkce/ <https://www.oauth.com/oauth2-servers/pkce/> and https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-09.html#name-cross-site-request-forgery <https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-09.html#name-cross-site-request-forgery> (describing both approaches)

```go
func (c *Config) Client(ctx context.Context, t *Token) *http.Client
```

Client returns an HTTP client using the provided token. The token will auto-refresh as necessary. The underlying HTTP transport will be obtained using the provided context. The returned client and its Transport should not be modified.

```go
func (c *Config) DeviceAccessToken(ctx context.Context, da *DeviceAuthResponse, opts ...AuthCodeOption) (*Token, error)
```

DeviceAccessToken polls the server to exchange a device code for a token.

```go
func (c *Config) DeviceAuth(ctx context.Context, opts ...AuthCodeOption) (*DeviceAuthResponse, error)
```

DeviceAuth returns a device auth struct which contains a device code and authorization information provided for users to enter on another device.

```go

var config Config
ctx := context.Background()
response, err := config.DeviceAuth(ctx)
if err != nil {
	panic(err)
}
fmt.Printf("please enter code %s at %s\n", response.UserCode, response.VerificationURI)
token, err := config.DeviceAccessToken(ctx, response)
if err != nil {
	panic(err)
}
fmt.Println(token)

```

```go
func (c *Config) Exchange(ctx context.Context, code string, opts ...AuthCodeOption) (*Token, error)
```

Exchange converts an authorization code into a token.

It is used after a resource provider redirects the user back to the Redirect URI (the URL obtained from AuthCodeURL).

The provided context optionally controls which HTTP client is used. See the HTTPClient variable.
