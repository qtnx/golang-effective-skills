oauth2 package - golang.org/x/oauth2 - Go Packages

## Details

-     Valid go.mod <https://cs.opensource.google/go/x/oauth2/+/v0.36.0:/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   cs.opensource.google/go/x/oauth2  <https://cs.opensource.google/go/x/oauth2>

## Links

-    Report a Vulnerability  <https://go.dev/security/policy>
-    Open Source Insights  <https://deps.dev/go/golang.org%2Fx%2Foauth2/v0.36.0>
-    Code Wiki

##   README ¶

### OAuth2 for Go

 <https://pkg.go.dev/golang.org/x/oauth2>  <https://travis-ci.org/golang/oauth2>

oauth2 package contains a client implementation for OAuth 2.0 spec.

See pkg.go.dev for further documentation and examples.

- pkg.go.dev/golang.org/x/oauth2 <https://pkg.go.dev/golang.org/x/oauth2>
- pkg.go.dev/golang.org/x/oauth2/google <https://pkg.go.dev/golang.org/x/oauth2/google>

#### Policy for new endpoints

We no longer accept new provider-specific packages in this repo if all they do is add a single endpoint variable. If you just want to add a single endpoint, add it to the pkg.go.dev/golang.org/x/oauth2/endpoints <https://pkg.go.dev/golang.org/x/oauth2/endpoints> package.

#### Report Issues / Send Patches

The main issue tracker for the oauth2 repository is located at https://github.com/golang/oauth2/issues <https://github.com/golang/oauth2/issues>.

This repository uses Gerrit for code changes. To learn how to submit changes to this repository, see https://go.dev/doc/contribute <https://go.dev/doc/contribute>.

The git repository is https://go.googlesource.com/oauth2 <https://go.googlesource.com/oauth2>.

Note:

- Excluding trivial changes, all contributions should be connected to an existing issue.
- API changes must go through the change proposal process <https://go.dev/s/proposal-process> before they can be accepted.
- The code owners are listed at dev.golang.org/owners <https://dev.golang.org/owners#:~:text=x/oauth2>.

 Expand ▾ Collapse ▴

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

The code will be in the http.Request.FormValue("code"). Before calling Exchange, be sure to validate http.Request.FormValue("state") if you are using it to protect against CSRF attacks.

If using PKCE to protect against CSRF attacks, opts should include a VerifierOption.

```go
func (c *Config) PasswordCredentialsToken(ctx context.Context, username, password string) (*Token, error)
```

PasswordCredentialsToken converts a resource owner username and password pair into a token.

Per the RFC, this grant type should only be used "when there is a high degree of trust between the resource owner and the client (e.g., the client is part of the device operating system or a highly privileged application), and when other authorization grant types are not available." See https://tools.ietf.org/html/rfc6749#section-4.3 <https://tools.ietf.org/html/rfc6749#section-4.3> for more info.

The provided context optionally controls which HTTP client is used. See the HTTPClient variable.

```go
func (c *Config) TokenSource(ctx context.Context, t *Token) TokenSource
```

TokenSource returns a TokenSource that returns t until t expires, automatically refreshing it as necessary using the provided context.

Most users will use Config.Client instead.

```go
type DeviceAuthResponse struct {
	// DeviceCode
	DeviceCode string `json:"device_code"`
	// UserCode is the code the user should enter at the verification uri
	UserCode string `json:"user_code"`
	// VerificationURI is where user should enter the user code
	VerificationURI string `json:"verification_uri"`
	// VerificationURIComplete (if populated) includes the user code in the verification URI. This is typically shown to the user in non-textual form, such as a QR code.
	VerificationURIComplete string `json:"verification_uri_complete,omitempty"`
	// Expiry is when the device code and user code expire
	Expiry time.Time `json:"expires_in,omitempty"`
	// Interval is the duration in seconds that Poll should wait between requests
	Interval int64 `json:"interval,omitempty"`
}
```

DeviceAuthResponse describes a successful RFC 8628 <https://rfc-editor.org/rfc/rfc8628.html> Device Authorization Response https://datatracker.ietf.org/doc/html/rfc8628#section-3.2 <https://datatracker.ietf.org/doc/html/rfc8628#section-3.2>

```go
func (d DeviceAuthResponse) MarshalJSON() ([]byte, error)
```

```go
func (c *DeviceAuthResponse) UnmarshalJSON(data []byte) error
```

```go
type Endpoint struct {
	AuthURL       string
	DeviceAuthURL string
	TokenURL      string

	// AuthStyle optionally specifies how the endpoint wants the
	// client ID & client secret sent. The zero value means to
	// auto-detect.
	AuthStyle AuthStyle
}
```

Endpoint represents an OAuth 2.0 provider's authorization and token endpoint URLs.

```go
type RetrieveError struct {
	Response *http.Response
	// Body is the body that was consumed by reading Response.Body.
	// It may be truncated.
	Body []byte
	// ErrorCode is RFC 6749 <https://rfc-editor.org/rfc/rfc6749.html>'s 'error' parameter.
	ErrorCode string
	// ErrorDescription is RFC 6749 <https://rfc-editor.org/rfc/rfc6749.html>'s 'error_description' parameter.
	ErrorDescription string
	// ErrorURI is RFC 6749 <https://rfc-editor.org/rfc/rfc6749.html>'s 'error_uri' parameter.
	ErrorURI string
}
```

RetrieveError is the error returned when the token endpoint returns a non-2XX HTTP status code or populates RFC 6749 <https://rfc-editor.org/rfc/rfc6749.html>'s 'error' parameter. https://datatracker.ietf.org/doc/html/rfc6749#section-5.2 <https://datatracker.ietf.org/doc/html/rfc6749#section-5.2>

```go
func (r *RetrieveError) Error() string
```

```go
type Token struct {
	// AccessToken is the token that authorizes and authenticates
	// the requests.
	AccessToken string `json:"access_token"`

	// TokenType is the type of token.
	// The Type method returns either this or "Bearer", the default.
	TokenType string `json:"token_type,omitempty"`

	// RefreshToken is a token that's used by the application
	// (as opposed to the user) to refresh the access token
	// if it expires.
	RefreshToken string `json:"refresh_token,omitempty"`

	// Expiry is the optional expiration time of the access token.
	//
	// If zero, [TokenSource] implementations will reuse the same
	// token forever and RefreshToken or equivalent
	// mechanisms for that TokenSource will not be used.
	Expiry time.Time `json:"expiry,omitempty"`

	// ExpiresIn is the OAuth2 wire format "expires_in" field,
	// which specifies how many seconds later the token expires,
	// relative to an unknown time base approximately around "now".
	// It is the application's responsibility to populate
	// `Expiry` from `ExpiresIn` when required.
	ExpiresIn int64 `json:"expires_in,omitempty"`
	// contains filtered or unexported fields
}
```

Token represents the credentials used to authorize the requests to access protected resources on the OAuth 2.0 provider's backend.

Most users of this package should not access fields of Token directly. They're exported mostly for use by related packages implementing derivative OAuth2 flows.

```go
func (t *Token) Extra(key string) any
```

Extra returns an extra field. Extra fields are key-value pairs returned by the server as part of the token retrieval response.

```go
func (t *Token) SetAuthHeader(r *http.Request)
```

SetAuthHeader sets the Authorization header to r using the access token in t.

This method is unnecessary when using Transport or an HTTP Client returned by this package.

```go
func (t *Token) Type() string
```

Type returns t.TokenType if non-empty, else "Bearer".

```go
func (t *Token) Valid() bool
```

Valid reports whether t is non-nil, has an AccessToken, and is not expired.

```go
func (t *Token) WithExtra(extra any) *Token
```

WithExtra returns a new Token that's a clone of t, but using the provided raw extra map. This is only intended for use by packages implementing derivative OAuth2 flows.

```go
type TokenSource interface {
	// Token returns a token or an error.
	// Token must be safe for concurrent use by multiple goroutines.
	// The returned Token must not be modified.
	Token() (*Token, error)
}
```

A TokenSource is anything that can return a token.

```go
func ReuseTokenSource(t *Token, src TokenSource) TokenSource
```

ReuseTokenSource returns a TokenSource which repeatedly returns the same token as long as it's valid, starting with t. When its cached token is invalid, a new token is obtained from src.

ReuseTokenSource is typically used to reuse tokens from a cache (such as a file on disk) between runs of a program, rather than obtaining new tokens unnecessarily.

The initial token t may be nil, in which case the TokenSource is wrapped in a caching version if it isn't one already. This also means it's always safe to wrap ReuseTokenSource around any other TokenSource without adverse effects.

```go
func ReuseTokenSourceWithExpiry(t *Token, src TokenSource, earlyExpiry time.Duration) TokenSource
```

ReuseTokenSourceWithExpiry returns a TokenSource that acts in the same manner as the TokenSource returned by ReuseTokenSource, except the expiry buffer is configurable. The expiration time of a token is calculated as t.Expiry.Add(-earlyExpiry).

```go
func StaticTokenSource(t *Token) TokenSource
```

StaticTokenSource returns a TokenSource that always returns the same token. Because the provided token t is never refreshed, StaticTokenSource is only useful for tokens that never expire.

```go
type Transport struct {
	// Source supplies the token to add to outgoing requests'
	// Authorization headers.
	Source TokenSource

	// Base is the base RoundTripper used to make HTTP requests.
	// If nil, http.DefaultTransport is used.
	Base http.RoundTripper
}
```

Transport is an http.RoundTripper that makes OAuth 2.0 HTTP requests, wrapping a base http.RoundTripper and adding an Authorization header with a token from the supplied TokenSource.

Transport is a low-level mechanism. Most code will use the higher-level Config.Client method instead.

```go
func (t *Transport) CancelRequest(req *http.Request)
```

CancelRequest does nothing. It used to be a legacy cancellation mechanism but now only logs on first use to warn that it's deprecated.

Deprecated: use contexts for cancellation instead.

```go
func (t *Transport) RoundTrip(req *http.Request) (*http.Response, error)
```

RoundTrip authorizes and authenticates the request with an access token from Transport's Source.

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/x/oauth2/+/v0.36.0:>

- deviceauth.go <https://cs.opensource.google/go/x/oauth2/+/v0.36.0:deviceauth.go>
- oauth2.go <https://cs.opensource.google/go/x/oauth2/+/v0.36.0:oauth2.go>
- pkce.go <https://cs.opensource.google/go/x/oauth2/+/v0.36.0:pkce.go>
- token.go <https://cs.opensource.google/go/x/oauth2/+/v0.36.0:token.go>
- transport.go <https://cs.opensource.google/go/x/oauth2/+/v0.36.0:transport.go>

##   Directories ¶
    Show internal   Expand all

      amazon
 Package amazon provides constants for using OAuth2 to access Amazon.

  Package amazon provides constants for using OAuth2 to access Amazon.    authhandler
 Package authhandler implements a TokenSource to support "three-legged OAuth 2.0" via a custom AuthorizationHandler.

  Package authhandler implements a TokenSource to support "three-legged OAuth 2.0" via a custom AuthorizationHandler.    bitbucket
 Package bitbucket provides constants for using OAuth2 to access Bitbucket.

  Package bitbucket provides constants for using OAuth2 to access Bitbucket.    cern
 Package cern provides constants for using OAuth2 to access CERN services.

  Package cern provides constants for using OAuth2 to access CERN services.    clientcredentials
 Package clientcredentials implements the OAuth2.0 "client credentials" token flow, also known as "two-legged OAuth 2.0".

  Package clientcredentials implements the OAuth2.0 "client credentials" token flow, also known as "two-legged OAuth 2.0".    endpoints
 Package endpoints provides constants for using OAuth2 to access various services.

  Package endpoints provides constants for using OAuth2 to access various services.    facebook
 Package facebook provides constants for using OAuth2 to access Facebook.

  Package facebook provides constants for using OAuth2 to access Facebook.    fitbit
 Package fitbit provides constants for using OAuth2 to access the Fitbit API.

  Package fitbit provides constants for using OAuth2 to access the Fitbit API.    foursquare
 Package foursquare provides constants for using OAuth2 to access Foursquare.

  Package foursquare provides constants for using OAuth2 to access Foursquare.    github
 Package github provides constants for using OAuth2 to access Github.

  Package github provides constants for using OAuth2 to access Github.    gitlab
 Package gitlab provides constants for using OAuth2 to access GitLab.

  Package gitlab provides constants for using OAuth2 to access GitLab.      google
 Package google provides support for making OAuth2 authorized and authenticated HTTP requests to Google APIs.

  Package google provides support for making OAuth2 authorized and authenticated HTTP requests to Google APIs.    downscope  Package downscope implements the ability to downscope, or restrict, the Identity and Access Management permissions that a short-lived Token can use.

  Package downscope implements the ability to downscope, or restrict, the Identity and Access Management permissions that a short-lived Token can use.    externalaccount  Package externalaccount provides support for creating workload identity federation and workforce identity federation token sources that can be used to access Google Cloud resources from external identity providers.

  Package externalaccount provides support for creating workload identity federation and workforce identity federation token sources that can be used to access Google Cloud resources from external identity providers.    internal/externalaccountauthorizeduser

      internal/impersonate

      internal/stsexchange

      heroku
 Package heroku provides constants for using OAuth2 to access Heroku.

  Package heroku provides constants for using OAuth2 to access Heroku.    hipchat
 Package hipchat provides constants for using OAuth2 to access HipChat.

  Package hipchat provides constants for using OAuth2 to access HipChat.    instagram
 Package instagram provides constants for using OAuth2 to access Instagram.

  Package instagram provides constants for using OAuth2 to access Instagram.    internal
 Package internal contains support packages for golang.org/x/oauth2.

  Package internal contains support packages for golang.org/x/oauth2.    jira
 Package jira provides claims and JWT signing for OAuth2 to access JIRA/Confluence.

  Package jira provides claims and JWT signing for OAuth2 to access JIRA/Confluence.    jws
 Package jws provides a partial implementation of JSON Web Signature encoding and decoding.

  Package jws provides a partial implementation of JSON Web Signature encoding and decoding.    jwt
 Package jwt implements the OAuth 2.0 JSON Web Token flow, commonly known as "two-legged OAuth 2.0".

  Package jwt implements the OAuth 2.0 JSON Web Token flow, commonly known as "two-legged OAuth 2.0".    kakao
 Package kakao provides constants for using OAuth2 to access Kakao.

  Package kakao provides constants for using OAuth2 to access Kakao.    linkedin
 Package linkedin provides constants for using OAuth2 to access LinkedIn.

  Package linkedin provides constants for using OAuth2 to access LinkedIn.    mailchimp
 Package mailchimp provides constants for using OAuth2 to access MailChimp.

  Package mailchimp provides constants for using OAuth2 to access MailChimp.    mailru
 Package mailru provides constants for using OAuth2 to access Mail.Ru.

  Package mailru provides constants for using OAuth2 to access Mail.Ru.    mediamath
 Package mediamath provides constants for using OAuth2 to access MediaMath.

  Package mediamath provides constants for using OAuth2 to access MediaMath.    microsoft
 Package microsoft provides constants for using OAuth2 to access Windows Live ID.

  Package microsoft provides constants for using OAuth2 to access Windows Live ID.    nokiahealth
 Package nokiahealth provides constants for using OAuth2 to access the Nokia Health Mate API.

  Package nokiahealth provides constants for using OAuth2 to access the Nokia Health Mate API.    odnoklassniki
 Package odnoklassniki provides constants for using OAuth2 to access Odnoklassniki.

  Package odnoklassniki provides constants for using OAuth2 to access Odnoklassniki.    paypal
 Package paypal provides constants for using OAuth2 to access PayPal.

  Package paypal provides constants for using OAuth2 to access PayPal.    slack
 Package slack provides constants for using OAuth2 to access Slack.

  Package slack provides constants for using OAuth2 to access Slack.    spotify
 Package spotify provides constants for using OAuth2 to access Spotify.

  Package spotify provides constants for using OAuth2 to access Spotify.    stackoverflow
 Package stackoverflow provides constants for using OAuth2 to access Stack Overflow.

  Package stackoverflow provides constants for using OAuth2 to access Stack Overflow.    twitch
 Package twitch provides constants for using OAuth2 to access Twitch.

  Package twitch provides constants for using OAuth2 to access Twitch.    uber
 Package uber provides constants for using OAuth2 to access Uber.

  Package uber provides constants for using OAuth2 to access Uber.    vk
 Package vk provides constants for using OAuth2 to access VK.com.

  Package vk provides constants for using OAuth2 to access VK.com.    yahoo
 Package yahoo provides constants for using OAuth2 to access Yahoo.

  Package yahoo provides constants for using OAuth2 to access Yahoo.    yandex
 Package yandex provides constants for using OAuth2 to access Yandex APIs.

  Package yandex provides constants for using OAuth2 to access Yandex APIs.

  Click to show internal directories.
  Click to hide internal directories.

  Close

     **?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
