---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/golang.org/x/oauth2"
source_path: "sources/raw/external/pkg-go-dev-golang-org-x-oauth2-dc2f217817.html"
license_ref: ""
---

##   Documentation ¶

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
