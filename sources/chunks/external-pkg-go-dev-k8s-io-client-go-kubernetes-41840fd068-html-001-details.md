---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/k8s.io/client-go/kubernetes"
source_path: "sources/raw/external/pkg-go-dev-k8s-io-client-go-kubernetes-41840fd068.html"
license_ref: ""
---

kubernetes package - k8s.io/client-go/kubernetes - Go Packages
## Details

-     Valid go.mod <https://github.com/kubernetes/client-go/tree/v0.36.1/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   github.com/kubernetes/client-go  <https://github.com/kubernetes/client-go>

##   Documentation ¶

Package kubernetes holds packages which implement a clientset for Kubernetes APIs.

-  type Clientset
-
-  func New(c rest.Interface) *Clientset
-  func NewForConfig(c *rest.Config) (*Clientset, error)
-  func NewForConfigAndClient(c *rest.Config, httpClient *http.Client) (*Clientset, error)
-  func NewForConfigOrDie(c *rest.Config) *Clientset

-
-  func (c *Clientset) AdmissionregistrationV1() admissionregistrationv1.AdmissionregistrationV1Interface
-  func (c *Clientset) AdmissionregistrationV1alpha1() admissionregistrationv1alpha1.AdmissionregistrationV1alpha1Interface
-  func (c *Clientset) AdmissionregistrationV1beta1() admissionregistrationv1beta1.AdmissionregistrationV1beta1Interface
-  func (c *Clientset) AppsV1() appsv1.AppsV1Interface
-  func (c *Clientset) AppsV1beta1() appsv1beta1.AppsV1beta1Interface
-  func (c *Clientset) AppsV1beta2() appsv1beta2.AppsV1beta2Interface
-  func (c *Clientset) AuthenticationV1() authenticationv1.AuthenticationV1Interface
-  func (c *Clientset) AuthenticationV1alpha1() authenticationv1alpha1.AuthenticationV1alpha1Interface
-  func (c *Clientset) AuthenticationV1beta1() authenticationv1beta1.AuthenticationV1beta1Interface
-  func (c *Clientset) AuthorizationV1() authorizationv1.AuthorizationV1Interface
-  func (c *Clientset) AuthorizationV1beta1() authorizationv1beta1.AuthorizationV1beta1Interface
-  func (c *Clientset) AutoscalingV1() autoscalingv1.AutoscalingV1Interface
-  func (c *Clientset) AutoscalingV2() autoscalingv2.AutoscalingV2Interface
-  func (c *Clientset) BatchV1() batchv1.BatchV1Interface
-  func (c *Clientset) BatchV1beta1() batchv1beta1.BatchV1beta1Interface
-  func (c *Clientset) CertificatesV1() certificatesv1.CertificatesV1Interface
-  func (c *Clientset) CertificatesV1alpha1() certificatesv1alpha1.CertificatesV1alpha1Interface
-  func (c *Clientset) CertificatesV1beta1() certificatesv1beta1.CertificatesV1beta1Interface
-  func (c *Clientset) CoordinationV1() coordinationv1.CoordinationV1Interface
-  func (c *Clientset) CoordinationV1alpha2() coordinationv1alpha2.CoordinationV1alpha2Interface
-  func (c *Clientset) CoordinationV1beta1() coordinationv1beta1.CoordinationV1beta1Interface
-  func (c *Clientset) CoreV1() corev1.CoreV1Interface
-  func (c *Clientset) Discovery() discovery.DiscoveryInterface
-  func (c *Clientset) DiscoveryV1() discoveryv1.DiscoveryV1Interface
-  func (c *Clientset) DiscoveryV1beta1() discoveryv1beta1.DiscoveryV1beta1Interface
-  func (c *Clientset) EventsV1() eventsv1.EventsV1Interface
-  func (c *Clientset) EventsV1beta1() eventsv1beta1.EventsV1beta1Interface
-  func (c *Clientset) ExtensionsV1beta1() extensionsv1beta1.ExtensionsV1beta1Interface
-  func (c *Clientset) FlowcontrolV1() flowcontrolv1.FlowcontrolV1Interface
-  func (c *Clientset) FlowcontrolV1beta1() flowcontrolv1beta1.FlowcontrolV1beta1Interface
-  func (c *Clientset) FlowcontrolV1beta2() flowcontrolv1beta2.FlowcontrolV1beta2Interface
-  func (c *Clientset) FlowcontrolV1beta3() flowcontrolv1beta3.FlowcontrolV1beta3Interface
-  func (c *Clientset) InternalV1alpha1() internalv1alpha1.InternalV1alpha1Interface
-  func (c *Clientset) NetworkingV1() networkingv1.NetworkingV1Interface
-  func (c *Clientset) NetworkingV1beta1() networkingv1beta1.NetworkingV1beta1Interface
-  func (c *Clientset) NodeV1() nodev1.NodeV1Interface
-  func (c *Clientset) NodeV1alpha1() nodev1alpha1.NodeV1alpha1Interface
-  func (c *Clientset) NodeV1beta1() nodev1beta1.NodeV1beta1Interface
-  func (c *Clientset) PolicyV1() policyv1.PolicyV1Interface
-  func (c *Clientset) PolicyV1beta1() policyv1beta1.PolicyV1beta1Interface
-  func (c *Clientset) RbacV1() rbacv1.RbacV1Interface
-  func (c *Clientset) RbacV1alpha1() rbacv1alpha1.RbacV1alpha1Interface
-  func (c *Clientset) RbacV1beta1() rbacv1beta1.RbacV1beta1Interface
-  func (c *Clientset) ResourceV1() resourcev1.ResourceV1Interface
-  func (c *Clientset) ResourceV1alpha3() resourcev1alpha3.ResourceV1alpha3Interface
-  func (c *Clientset) ResourceV1beta1() resourcev1beta1.ResourceV1beta1Interface
-  func (c *Clientset) ResourceV1beta2() resourcev1beta2.ResourceV1beta2Interface
-  func (c *Clientset) SchedulingV1() schedulingv1.SchedulingV1Interface
-  func (c *Clientset) SchedulingV1alpha2() schedulingv1alpha2.SchedulingV1alpha2Interface
-  func (c *Clientset) SchedulingV1beta1() schedulingv1beta1.SchedulingV1beta1Interface
-  func (c *Clientset) StorageV1() storagev1.StorageV1Interface
-  func (c *Clientset) StorageV1alpha1() storagev1alpha1.StorageV1alpha1Interface
-  func (c *Clientset) StorageV1beta1() storagev1beta1.StorageV1beta1Interface
-  func (c *Clientset) StoragemigrationV1beta1() storagemigrationv1beta1.StoragemigrationV1beta1Interface

-  type Interface

This section is empty.

This section is empty.

This section is empty.

```go
type Clientset struct {
	*discovery.DiscoveryClient
	// contains filtered or unexported fields
}
```

Clientset contains the clients for groups.

```go
func New(c rest.Interface) *Clientset
```

New creates a new Clientset for the given RESTClient.

```go
func NewForConfig(c *rest.Config) (*Clientset, error)
```

NewForConfig creates a new Clientset for the given config. If config's RateLimiter is not set and QPS and Burst are acceptable, NewForConfig will generate a rate-limiter in configShallowCopy. NewForConfig is equivalent to NewForConfigAndClient(c, httpClient), where httpClient was generated with rest.HTTPClientFor(c).

```go
func NewForConfigAndClient(c *rest.Config, httpClient *http.Client) (*Clientset, error)
```

NewForConfigAndClient creates a new Clientset for the given config and http client. Note the http client provided takes precedence over the configured transport values. If config's RateLimiter is not set and QPS and Burst are acceptable, NewForConfigAndClient will generate a rate-limiter in configShallowCopy.

```go
func NewForConfigOrDie(c *rest.Config) *Clientset
```

NewForConfigOrDie creates a new Clientset for the given config and panics if there is an error in the config.

```go
func (c *Clientset) AdmissionregistrationV1() admissionregistrationv1.AdmissionregistrationV1Interface
```

AdmissionregistrationV1 retrieves the AdmissionregistrationV1Client

```go
func (c *Clientset) AdmissionregistrationV1alpha1() admissionregistrationv1alpha1.AdmissionregistrationV1alpha1Interface
```

AdmissionregistrationV1alpha1 retrieves the AdmissionregistrationV1alpha1Client

```go
func (c *Clientset) AdmissionregistrationV1beta1() admissionregistrationv1beta1.AdmissionregistrationV1beta1Interface
```

AdmissionregistrationV1beta1 retrieves the AdmissionregistrationV1beta1Client

```go
func (c *Clientset) AppsV1() appsv1.AppsV1Interface
```

AppsV1 retrieves the AppsV1Client

```go
func (c *Clientset) AppsV1beta1() appsv1beta1.AppsV1beta1Interface
```

AppsV1beta1 retrieves the AppsV1beta1Client

```go
func (c *Clientset) AppsV1beta2() appsv1beta2.AppsV1beta2Interface
```

AppsV1beta2 retrieves the AppsV1beta2Client

```go
func (c *Clientset) AuthenticationV1() authenticationv1.AuthenticationV1Interface
```

AuthenticationV1 retrieves the AuthenticationV1Client

```go
func (c *Clientset) AuthenticationV1alpha1() authenticationv1alpha1.AuthenticationV1alpha1Interface
```

AuthenticationV1alpha1 retrieves the AuthenticationV1alpha1Client

```go
func (c *Clientset) AuthenticationV1beta1() authenticationv1beta1.AuthenticationV1beta1Interface
```

AuthenticationV1beta1 retrieves the AuthenticationV1beta1Client

```go
func (c *Clientset) AuthorizationV1() authorizationv1.AuthorizationV1Interface
```

AuthorizationV1 retrieves the AuthorizationV1Client

```go
func (c *Clientset) AuthorizationV1beta1() authorizationv1beta1.AuthorizationV1beta1Interface
```

AuthorizationV1beta1 retrieves the AuthorizationV1beta1Client

```go
func (c *Clientset) AutoscalingV1() autoscalingv1.AutoscalingV1Interface
```

AutoscalingV1 retrieves the AutoscalingV1Client

```go
func (c *Clientset) AutoscalingV2() autoscalingv2.AutoscalingV2Interface
```

AutoscalingV2 retrieves the AutoscalingV2Client

```go
func (c *Clientset) BatchV1() batchv1.BatchV1Interface
```

BatchV1 retrieves the BatchV1Client

```go
func (c *Clientset) BatchV1beta1() batchv1beta1.BatchV1beta1Interface
```

BatchV1beta1 retrieves the BatchV1beta1Client

```go
func (c *Clientset) CertificatesV1() certificatesv1.CertificatesV1Interface
```

CertificatesV1 retrieves the CertificatesV1Client

```go
func (c *Clientset) CertificatesV1alpha1() certificatesv1alpha1.CertificatesV1alpha1Interface
```

CertificatesV1alpha1 retrieves the CertificatesV1alpha1Client

```go
func (c *Clientset) CertificatesV1beta1() certificatesv1beta1.CertificatesV1beta1Interface
```

CertificatesV1beta1 retrieves the CertificatesV1beta1Client

```go
func (c *Clientset) CoordinationV1() coordinationv1.CoordinationV1Interface
```

CoordinationV1 retrieves the CoordinationV1Client

```go
func (c *Clientset) CoordinationV1alpha2() coordinationv1alpha2.CoordinationV1alpha2Interface
```

CoordinationV1alpha2 retrieves the CoordinationV1alpha2Client

```go
func (c *Clientset) CoordinationV1beta1() coordinationv1beta1.CoordinationV1beta1Interface
```

CoordinationV1beta1 retrieves the CoordinationV1beta1Client

```go
func (c *Clientset) CoreV1() corev1.CoreV1Interface
```

CoreV1 retrieves the CoreV1Client

```go
func (c *Clientset) Discovery() discovery.DiscoveryInterface
```

Discovery retrieves the DiscoveryClient

```go
func (c *Clientset) DiscoveryV1() discoveryv1.DiscoveryV1Interface
```

DiscoveryV1 retrieves the DiscoveryV1Client

```go
func (c *Clientset) DiscoveryV1beta1() discoveryv1beta1.DiscoveryV1beta1Interface
```

DiscoveryV1beta1 retrieves the DiscoveryV1beta1Client

```go
func (c *Clientset) EventsV1() eventsv1.EventsV1Interface
```

EventsV1 retrieves the EventsV1Client

```go
func (c *Clientset) EventsV1beta1() eventsv1beta1.EventsV1beta1Interface
```

EventsV1beta1 retrieves the EventsV1beta1Client

```go
func (c *Clientset) ExtensionsV1beta1() extensionsv1beta1.ExtensionsV1beta1Interface
```

ExtensionsV1beta1 retrieves the ExtensionsV1beta1Client

```go
func (c *Clientset) FlowcontrolV1() flowcontrolv1.FlowcontrolV1Interface
```

FlowcontrolV1 retrieves the FlowcontrolV1Client

```go
func (c *Clientset) FlowcontrolV1beta1() flowcontrolv1beta1.FlowcontrolV1beta1Interface
```

FlowcontrolV1beta1 retrieves the FlowcontrolV1beta1Client

```go
func (c *Clientset) FlowcontrolV1beta2() flowcontrolv1beta2.FlowcontrolV1beta2Interface
```

FlowcontrolV1beta2 retrieves the FlowcontrolV1beta2Client

```go
func (c *Clientset) FlowcontrolV1beta3() flowcontrolv1beta3.FlowcontrolV1beta3Interface
```

FlowcontrolV1beta3 retrieves the FlowcontrolV1beta3Client

```go
func (c *Clientset) InternalV1alpha1() internalv1alpha1.InternalV1alpha1Interface
```

InternalV1alpha1 retrieves the InternalV1alpha1Client

```go
func (c *Clientset) NetworkingV1() networkingv1.NetworkingV1Interface
```

NetworkingV1 retrieves the NetworkingV1Client

```go
func (c *Clientset) NetworkingV1beta1() networkingv1beta1.NetworkingV1beta1Interface
```

NetworkingV1beta1 retrieves the NetworkingV1beta1Client

```go
func (c *Clientset) NodeV1() nodev1.NodeV1Interface
```

NodeV1 retrieves the NodeV1Client

```go
func (c *Clientset) NodeV1alpha1() nodev1alpha1.NodeV1alpha1Interface
```

NodeV1alpha1 retrieves the NodeV1alpha1Client

```go
func (c *Clientset) NodeV1beta1() nodev1beta1.NodeV1beta1Interface
```

NodeV1beta1 retrieves the NodeV1beta1Client

```go
func (c *Clientset) PolicyV1() policyv1.PolicyV1Interface
```

PolicyV1 retrieves the PolicyV1Client

```go
func (c *Clientset) PolicyV1beta1() policyv1beta1.PolicyV1beta1Interface
```

PolicyV1beta1 retrieves the PolicyV1beta1Client

```go
func (c *Clientset) RbacV1() rbacv1.RbacV1Interface
```

RbacV1 retrieves the RbacV1Client

```go
func (c *Clientset) RbacV1alpha1() rbacv1alpha1.RbacV1alpha1Interface
```

RbacV1alpha1 retrieves the RbacV1alpha1Client

```go
func (c *Clientset) RbacV1beta1() rbacv1beta1.RbacV1beta1Interface
```

RbacV1beta1 retrieves the RbacV1beta1Client

```go
func (c *Clientset) ResourceV1() resourcev1.ResourceV1Interface
```

ResourceV1 retrieves the ResourceV1Client

```go
func (c *Clientset) ResourceV1alpha3() resourcev1alpha3.ResourceV1alpha3Interface
```

ResourceV1alpha3 retrieves the ResourceV1alpha3Client

```go
func (c *Clientset) ResourceV1beta1() resourcev1beta1.ResourceV1beta1Interface
```

ResourceV1beta1 retrieves the ResourceV1beta1Client

```go
func (c *Clientset) ResourceV1beta2() resourcev1beta2.ResourceV1beta2Interface
```

ResourceV1beta2 retrieves the ResourceV1beta2Client

```go
func (c *Clientset) SchedulingV1() schedulingv1.SchedulingV1Interface
```

SchedulingV1 retrieves the SchedulingV1Client

```go
func (c *Clientset) SchedulingV1alpha2() schedulingv1alpha2.SchedulingV1alpha2Interface
```

SchedulingV1alpha2 retrieves the SchedulingV1alpha2Client

```go
func (c *Clientset) SchedulingV1beta1() schedulingv1beta1.SchedulingV1beta1Interface
```

SchedulingV1beta1 retrieves the SchedulingV1beta1Client

```go
func (c *Clientset) StorageV1() storagev1.StorageV1Interface
```

StorageV1 retrieves the StorageV1Client

```go
func (c *Clientset) StorageV1alpha1() storagev1alpha1.StorageV1alpha1Interface
```

StorageV1alpha1 retrieves the StorageV1alpha1Client

```go
func (c *Clientset) StorageV1beta1() storagev1beta1.StorageV1beta1Interface
```

StorageV1beta1 retrieves the StorageV1beta1Client

```go
func (c *Clientset) StoragemigrationV1beta1() storagemigrationv1beta1.StoragemigrationV1beta1Interface
```

StoragemigrationV1beta1 retrieves the StoragemigrationV1beta1Client

```go
type Interface interface {
	Discovery() discovery.DiscoveryInterface
	AdmissionregistrationV1() admissionregistrationv1.AdmissionregistrationV1Interface
	AdmissionregistrationV1alpha1() admissionregistrationv1alpha1.AdmissionregistrationV1alpha1Interface
	AdmissionregistrationV1beta1() admissionregistrationv1beta1.AdmissionregistrationV1beta1Interface
	InternalV1alpha1() internalv1alpha1.InternalV1alpha1Interface
	AppsV1() appsv1.AppsV1Interface
	AppsV1beta1() appsv1beta1.AppsV1beta1Interface
	AppsV1beta2() appsv1beta2.AppsV1beta2Interface
	AuthenticationV1() authenticationv1.AuthenticationV1Interface
	AuthenticationV1alpha1() authenticationv1alpha1.AuthenticationV1alpha1Interface
	AuthenticationV1beta1() authenticationv1beta1.AuthenticationV1beta1Interface
	AuthorizationV1() authorizationv1.AuthorizationV1Interface
	AuthorizationV1beta1() authorizationv1beta1.AuthorizationV1beta1Interface
	AutoscalingV1() autoscalingv1.AutoscalingV1Interface
	AutoscalingV2() autoscalingv2.AutoscalingV2Interface
	BatchV1() batchv1.BatchV1Interface
	BatchV1beta1() batchv1beta1.BatchV1beta1Interface
	CertificatesV1() certificatesv1.CertificatesV1Interface
	CertificatesV1beta1() certificatesv1beta1.CertificatesV1beta1Interface
	CertificatesV1alpha1() certificatesv1alpha1.CertificatesV1alpha1Interface
	CoordinationV1alpha2() coordinationv1alpha2.CoordinationV1alpha2Interface
	CoordinationV1beta1() coordinationv1beta1.CoordinationV1beta1Interface
	CoordinationV1() coordinationv1.CoordinationV1Interface
	CoreV1() corev1.CoreV1Interface
	DiscoveryV1() discoveryv1.DiscoveryV1Interface
	DiscoveryV1beta1() discoveryv1beta1.DiscoveryV1beta1Interface
	EventsV1() eventsv1.EventsV1Interface
	EventsV1beta1() eventsv1beta1.EventsV1beta1Interface
	ExtensionsV1beta1() extensionsv1beta1.ExtensionsV1beta1Interface
	FlowcontrolV1() flowcontrolv1.FlowcontrolV1Interface
	FlowcontrolV1beta1() flowcontrolv1beta1.FlowcontrolV1beta1Interface
	FlowcontrolV1beta2() flowcontrolv1beta2.FlowcontrolV1beta2Interface
	FlowcontrolV1beta3() flowcontrolv1beta3.FlowcontrolV1beta3Interface
	NetworkingV1() networkingv1.NetworkingV1Interface
	NetworkingV1beta1() networkingv1beta1.NetworkingV1beta1Interface
	NodeV1() nodev1.NodeV1Interface
	NodeV1alpha1() nodev1alpha1.NodeV1alpha1Interface
	NodeV1beta1() nodev1beta1.NodeV1beta1Interface
	PolicyV1() policyv1.PolicyV1Interface
	PolicyV1beta1() policyv1beta1.PolicyV1beta1Interface
	RbacV1() rbacv1.RbacV1Interface
	RbacV1beta1() rbacv1beta1.RbacV1beta1Interface
	RbacV1alpha1() rbacv1alpha1.RbacV1alpha1Interface
	ResourceV1() resourcev1.ResourceV1Interface
	ResourceV1beta2() resourcev1beta2.ResourceV1beta2Interface
	ResourceV1beta1() resourcev1beta1.ResourceV1beta1Interface
	ResourceV1alpha3() resourcev1alpha3.ResourceV1alpha3Interface
	SchedulingV1alpha2() schedulingv1alpha2.SchedulingV1alpha2Interface
	SchedulingV1beta1() schedulingv1beta1.SchedulingV1beta1Interface
	SchedulingV1() schedulingv1.SchedulingV1Interface
	StorageV1beta1() storagev1beta1.StorageV1beta1Interface
	StorageV1() storagev1.StorageV1Interface
	StorageV1alpha1() storagev1alpha1.StorageV1alpha1Interface
	StoragemigrationV1beta1() storagemigrationv1beta1.StoragemigrationV1beta1Interface
}
```
