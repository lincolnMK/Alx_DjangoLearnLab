kings is here testing django

for permissions and groups:
add models 
add custom permissions in the models 
enforce permissions through views 
eg view, edit, delete, 

views that do action as the specified in the permissions should first of all check if user has perms.

---

## Security Settings

### CSRF Token Protection
- **CSRF_COOKIE_SECURE = True**: Ensures CSRF cookies are only transmitted over HTTPS, preventing interception over unencrypted connections
- **CsrfViewMiddleware**: Enabled in middleware to validate CSRF tokens on all POST, PUT, PATCH, and DELETE requests, protecting against Cross-Site Request Forgery attacks

### Session Security
- **SESSION_COOKIE_SECURE = True**: Ensures session cookies are only sent over HTTPS, protecting user authentication tokens from being exposed over insecure connections

### HTTPS & SSL/TLS
- **SECURE_SSL_REDIRECT = True**: Automatically redirects all non-HTTPS requests to HTTPS, ensuring all communication is encrypted
- **SECURE_HSTS_SECONDS = 31536000**: Enables HTTP Strict-Transport-Security (HSTS) for 1 year, forcing browsers to always use HTTPS
- **SECURE_HSTS_INCLUDE_SUBDOMAINS = True**: Applies HSTS policy to all subdomains
- **SECURE_HSTS_PRELOAD = True**: Allows the domain to be added to the HSTS preload list for maximum protection
- **SECURE_PROXY_SSL_HEADER**: Trusts the X-Forwarded-Proto header from proxies to properly detect HTTPS connections

### XSS & Content Handling
- **SECURE_BROWSER_XSS_FILTER = True**: Enables the browser's built-in XSS filter to block reflected XSS attacks
- **SECURE_CONTENT_TYPE_NOSNIFF = True**: Prevents browsers from MIME-sniffing responses, forcing them to respect the declared content-type header

### Clickjacking Protection
- **X_FRAME_OPTIONS = 'DENY'**: Prevents the site from being framed in any context, protecting against clickjacking attacks where users are tricked into clicking hidden elements

### Content Security Policy (CSP)
A strict CSP has been implemented with the following directives:
- **CSP_DEFAULT_SRC = ('self')**: All content defaults to same-origin only
- **CSP_SCRIPT_SRC = ('self')**: Only scripts from the same origin are allowed (prevents inline scripts and external script injection)
- **CSP_STYLE_SRC = ('self')**: Only stylesheets from the same origin are allowed
- **CSP_IMG_SRC = ('self', 'data:')**: Images from same origin and data URIs only
- **CSP_FONT_SRC = ('self')**: Fonts from same origin only
- **CSP_CONNECT_SRC = ('self')**: AJAX/WebSocket connections to same origin only
- **CSP_FRAME_SRC = ('none')**: No framing allowed
- **CSP_OBJECT_SRC = ('none')**: No Flash or other plugins allowed
- **CSP_BASE_URI = ('self')**: Base tag can only reference same origin
- **CSP_FORM_ACTION = ('self')**: Forms can only submit to same origin

### Other Security Settings
- **DEBUG = False**: Production setting to prevent sensitive information leakage in error pages
- **SECURE_BROWSER_XSS_FILTER = True**: Activates browser XSS protection mechanism
- **X_FRAME_OPTIONS = 'DENY'**: Prevents clickjacking attacks by disallowing any framing of the application
