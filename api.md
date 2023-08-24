# Shared Types

```python
from tecmie.types import AuditDto, ReferenceIDDto
```

# Root

Methods:

- <code title="get /">client.root.<a href="./src/tecmie/resources/root.py">retrieve</a>() -> None</code>

# Auth

Types:

```python
from tecmie.types import (
    AuthLoginResponse,
    AuthSignupResponse,
    AuthVerifyBillingResponse,
)
```

Methods:

- <code title="post /auth/login">client.auth.<a href="./src/tecmie/resources/auth/auth.py">login</a>(\*\*<a href="src/tecmie/types/auth_login_params.py">params</a>) -> <a href="./src/tecmie/types/auth_login_response.py">AuthLoginResponse</a></code>
- <code title="post /auth/signup">client.auth.<a href="./src/tecmie/resources/auth/auth.py">signup</a>(\*\*<a href="src/tecmie/types/auth_signup_params.py">params</a>) -> <a href="./src/tecmie/types/auth_signup_response.py">AuthSignupResponse</a></code>
- <code title="post /auth/verify_billing">client.auth.<a href="./src/tecmie/resources/auth/auth.py">verify_billing</a>(\*\*<a href="src/tecmie/types/auth_verify_billing_params.py">params</a>) -> <a href="./src/tecmie/types/auth_verify_billing_response.py">AuthVerifyBillingResponse</a></code>

## Token

Types:

```python
from tecmie.types.auth import TokenRefreshResponse
```

Methods:

- <code title="post /auth/token/refresh">client.auth.token.<a href="./src/tecmie/resources/auth/token.py">refresh</a>(\*\*<a href="src/tecmie/types/auth/token_refresh_params.py">params</a>) -> <a href="./src/tecmie/types/auth/token_refresh_response.py">TokenRefreshResponse</a></code>

## Recovery

### Login

Methods:

- <code title="post /auth/recovery/login">client.auth.recovery.login.<a href="./src/tecmie/resources/auth/recovery/login.py">create</a>(\*\*<a href="src/tecmie/types/auth/recovery/login_create_params.py">params</a>) -> None</code>

### Password

Methods:

- <code title="post /auth/recovery/password">client.auth.recovery.password.<a href="./src/tecmie/resources/auth/recovery/password.py">create</a>(\*\*<a href="src/tecmie/types/auth/recovery/password_create_params.py">params</a>) -> None</code>
- <code title="patch /auth/recovery/password">client.auth.recovery.password.<a href="./src/tecmie/resources/auth/recovery/password.py">update</a>(\*\*<a href="src/tecmie/types/auth/recovery/password_update_params.py">params</a>) -> None</code>

### Passcode

Methods:

- <code title="get /auth/recovery/passcode/{passcode}">client.auth.recovery.passcode.<a href="./src/tecmie/resources/auth/recovery/passcode.py">retrieve</a>(passcode) -> None</code>

# Space

## Members

Methods:

- <code title="get /space/{space_id}/members/{member_uid}">client.space.members.<a href="./src/tecmie/resources/space/members.py">retrieve</a>(space_id, member_uid) -> None</code>
- <code title="get /space/{space_id}/members">client.space.members.<a href="./src/tecmie/resources/space/members.py">list</a>(space_id) -> None</code>

## Tokens

Types:

```python
from tecmie.types.space import TokenCreateResponse, TokenListResponse
```

Methods:

- <code title="post /space/{space_sid}/tokens">client.space.tokens.<a href="./src/tecmie/resources/space/tokens.py">create</a>(space_sid, \*\*<a href="src/tecmie/types/space/token_create_params.py">params</a>) -> <a href="./src/tecmie/types/space/token_create_response.py">TokenCreateResponse</a></code>
- <code title="get /space/{space_sid}/tokens">client.space.tokens.<a href="./src/tecmie/resources/space/tokens.py">list</a>(space_sid) -> <a href="./src/tecmie/types/space/token_list_response.py">TokenListResponse</a></code>
- <code title="delete /space/{space_sid}/tokens/{token_id}">client.space.tokens.<a href="./src/tecmie/resources/space/tokens.py">delete</a>(space_sid, token_id) -> None</code>

# Wspaces

Types:

```python
from tecmie.types import WorkspaceDto
```

Methods:

- <code title="post /wspace">client.wspaces.<a href="./src/tecmie/resources/wspaces.py">create</a>(\*\*<a href="src/tecmie/types/wspace_create_params.py">params</a>) -> <a href="./src/tecmie/types/workspace_dto.py">WorkspaceDto</a></code>
- <code title="get /wspace/{id}">client.wspaces.<a href="./src/tecmie/resources/wspaces.py">retrieve</a>(id, \*\*<a href="src/tecmie/types/wspace_retrieve_params.py">params</a>) -> <a href="./src/tecmie/types/workspace_dto.py">WorkspaceDto</a></code>
- <code title="patch /wspace/{id}">client.wspaces.<a href="./src/tecmie/resources/wspaces.py">update</a>(path_id, \*\*<a href="src/tecmie/types/wspace_update_params.py">params</a>) -> <a href="./src/tecmie/types/workspace_dto.py">WorkspaceDto</a></code>

# Roles

Types:

```python
from tecmie.types import (
    RoleDto,
    RolePaginatedDto,
    RoleListResponse,
    RoleDeleteResponse,
    RoleBulkCreateResponse,
)
```

Methods:

- <code title="post /role">client.roles.<a href="./src/tecmie/resources/roles.py">create</a>(\*\*<a href="src/tecmie/types/role_create_params.py">params</a>) -> <a href="./src/tecmie/types/role_dto.py">RoleDto</a></code>
- <code title="get /role/{id}">client.roles.<a href="./src/tecmie/resources/roles.py">retrieve</a>(id, \*\*<a href="src/tecmie/types/role_retrieve_params.py">params</a>) -> <a href="./src/tecmie/types/role_dto.py">RoleDto</a></code>
- <code title="patch /role/{id}">client.roles.<a href="./src/tecmie/resources/roles.py">update</a>(id, \*\*<a href="src/tecmie/types/role_update_params.py">params</a>) -> <a href="./src/tecmie/types/role_dto.py">RoleDto</a></code>
- <code title="get /role">client.roles.<a href="./src/tecmie/resources/roles.py">list</a>(\*\*<a href="src/tecmie/types/role_list_params.py">params</a>) -> <a href="./src/tecmie/types/role_list_response.py">RoleListResponse</a></code>
- <code title="delete /role/{id}">client.roles.<a href="./src/tecmie/resources/roles.py">delete</a>(id) -> <a href="./src/tecmie/types/role_delete_response.py">object</a></code>
- <code title="post /role/bulk">client.roles.<a href="./src/tecmie/resources/roles.py">bulk_create</a>(\*\*<a href="src/tecmie/types/role_bulk_create_params.py">params</a>) -> <a href="./src/tecmie/types/role_bulk_create_response.py">RoleBulkCreateResponse</a></code>

# RoleAssignments

Types:

```python
from tecmie.types import RoleAssignment, RoleAssignmentDto, RoleAssignmentPaginatedDto
```

Methods:

- <code title="post /role-assignment/{assignment}">client.role_assignments.<a href="./src/tecmie/resources/role_assignments/role_assignments.py">create</a>(assignment, \*\*<a href="src/tecmie/types/role_assignment_create_params.py">params</a>) -> <a href="./src/tecmie/types/role_assignment_dto.py">RoleAssignmentDto</a></code>
- <code title="get /role-assignment/{assignment}/{id}">client.role_assignments.<a href="./src/tecmie/resources/role_assignments/role_assignments.py">retrieve</a>(assignment, id, \*\*<a href="src/tecmie/types/role_assignment_retrieve_params.py">params</a>) -> <a href="./src/tecmie/types/role_assignment_dto.py">RoleAssignmentDto</a></code>
- <code title="delete /role-assignment/{assignment}/{id}">client.role_assignments.<a href="./src/tecmie/resources/role_assignments/role_assignments.py">delete</a>(assignment, id) -> <a href="./src/tecmie/types/role_assignment.py">object</a></code>

## Bulk

Types:

```python
from tecmie.types.role_assignments import BulkCreateResponse
```

Methods:

- <code title="post /role-assignment/{assignment}/bulk">client.role_assignments.bulk.<a href="./src/tecmie/resources/role_assignments/bulk.py">create</a>(assignment, \*\*<a href="src/tecmie/types/role_assignments/bulk_create_params.py">params</a>) -> <a href="./src/tecmie/types/role_assignments/bulk_create_response.py">BulkCreateResponse</a></code>

# Invitations

Types:

```python
from tecmie.types import (
    InvitationDto,
    InvitationPaginatedDto,
    InvitationListResponse,
    InvitationDeleteResponse,
)
```

Methods:

- <code title="post /invitation">client.invitations.<a href="./src/tecmie/resources/invitations.py">create</a>(\*\*<a href="src/tecmie/types/invitation_create_params.py">params</a>) -> <a href="./src/tecmie/types/invitation_dto.py">InvitationDto</a></code>
- <code title="get /invitation/{id}">client.invitations.<a href="./src/tecmie/resources/invitations.py">retrieve</a>(id, \*\*<a href="src/tecmie/types/invitation_retrieve_params.py">params</a>) -> <a href="./src/tecmie/types/invitation_dto.py">InvitationDto</a></code>
- <code title="get /invitation">client.invitations.<a href="./src/tecmie/resources/invitations.py">list</a>(\*\*<a href="src/tecmie/types/invitation_list_params.py">params</a>) -> <a href="./src/tecmie/types/invitation_list_response.py">InvitationListResponse</a></code>
- <code title="delete /invitation/{id}">client.invitations.<a href="./src/tecmie/resources/invitations.py">delete</a>(id) -> <a href="./src/tecmie/types/invitation_delete_response.py">object</a></code>

# InvitationAcceptance

Methods:

- <code title="get /invitation_acceptance/{code}">client.invitation_acceptance.<a href="./src/tecmie/resources/invitation_acceptance.py">retrieve</a>(code, \*\*<a href="src/tecmie/types/invitation_acceptance_retrieve_params.py">params</a>) -> None</code>
- <code title="patch /invitation_acceptance/{code}">client.invitation_acceptance.<a href="./src/tecmie/resources/invitation_acceptance.py">update</a>(code, \*\*<a href="src/tecmie/types/invitation_acceptance_update_params.py">params</a>) -> None</code>

# InvitationReattempt

Methods:

- <code title="post /invitation_reattempt/{code}">client.invitation_reattempt.<a href="./src/tecmie/resources/invitation_reattempt.py">create</a>(code) -> None</code>

# Users

Types:

```python
from tecmie.types import UserDto, UserPaginatedDto, UserListResponse
```

Methods:

- <code title="get /user/{id}">client.users.<a href="./src/tecmie/resources/users/users.py">retrieve</a>(id, \*\*<a href="src/tecmie/types/user_retrieve_params.py">params</a>) -> <a href="./src/tecmie/types/user_dto.py">UserDto</a></code>
- <code title="get /user">client.users.<a href="./src/tecmie/resources/users/users.py">list</a>(\*\*<a href="src/tecmie/types/user_list_params.py">params</a>) -> <a href="./src/tecmie/types/user_list_response.py">UserListResponse</a></code>

## Recover

Types:

```python
from tecmie.types.users import UserRecover
```

Methods:

- <code title="patch /user/recover/{id}">client.users.recover.<a href="./src/tecmie/resources/users/recover.py">update</a>(id) -> <a href="./src/tecmie/types/users/user_recover.py">object</a></code>

# Aws

Types:

```python
from tecmie.types import AwsS3GetSignedURLResponse, AwsS3SignedURLPostSerialization
```

Methods:

- <code title="post /aws/get-signed-put-url">client.aws.<a href="./src/tecmie/resources/aws/aws.py">create_signed_put_url</a>(\*\*<a href="src/tecmie/types/aw_create_signed_put_url_params.py">params</a>) -> <a href="./src/tecmie/types/aws_s3_get_signed_url_response.py">AwsS3GetSignedURLResponse</a></code>

## Buckets

Types:

```python
from tecmie.types.aws import (
    AwsS3GetManyBucketsSerialization,
    AwsS3GetOneBucketObjectResponse,
    AwsS3Serialization,
    BucketBulkUploadResponse,
)
```

Methods:

- <code title="get /aws/buckets">client.aws.buckets.<a href="./src/tecmie/resources/aws/buckets/buckets.py">list</a>() -> <a href="./src/tecmie/types/aws/aws_s3_get_many_buckets_serialization.py">AwsS3GetManyBucketsSerialization</a></code>
- <code title="post /aws/buckets/bulk_upload">client.aws.buckets.<a href="./src/tecmie/resources/aws/buckets/buckets.py">bulk_upload</a>(\*\*<a href="src/tecmie/types/aws/bucket_bulk_upload_params.py">params</a>) -> <a href="./src/tecmie/types/aws/bucket_bulk_upload_response.py">BucketBulkUploadResponse</a></code>
- <code title="get /aws/buckets/{filename}">client.aws.buckets.<a href="./src/tecmie/resources/aws/buckets/buckets.py">retrieve_file</a>(filename) -> <a href="./src/tecmie/types/aws/aws_s3_get_one_bucket_object_response.py">AwsS3GetOneBucketObjectResponse</a></code>
- <code title="get /aws/buckets/{pathname}/{filename}">client.aws.buckets.<a href="./src/tecmie/resources/aws/buckets/buckets.py">retrieve_file_in_path</a>(pathname, filename) -> <a href="./src/tecmie/types/aws/aws_s3_get_one_bucket_object_response.py">AwsS3GetOneBucketObjectResponse</a></code>
- <code title="post /aws/buckets/upload">client.aws.buckets.<a href="./src/tecmie/resources/aws/buckets/buckets.py">upload</a>(\*\*<a href="src/tecmie/types/aws/bucket_upload_params.py">params</a>) -> <a href="./src/tecmie/types/aws/aws_s3_serialization.py">AwsS3Serialization</a></code>

### Health

Methods:

- <code title="get /aws/buckets/health">client.aws.buckets.health.<a href="./src/tecmie/resources/aws/buckets/health.py">retrieve</a>() -> None</code>

## Objects

Methods:

- <code title="get /aws/objects">client.aws.objects.<a href="./src/tecmie/resources/aws/objects.py">list</a>() -> None</code>

# Registry

## Resources

Methods:

- <code title="get /registry/resources">client.registry.resources.<a href="./src/tecmie/resources/registry/resources.py">list</a>() -> None</code>

## Actions

Methods:

- <code title="get /registry/actions">client.registry.actions.<a href="./src/tecmie/resources/registry/actions.py">list</a>() -> None</code>

# Features

Methods:

- <code title="get /features">client.features.<a href="./src/tecmie/resources/features.py">list</a>(\*\*<a href="src/tecmie/types/feature_list_params.py">params</a>) -> None</code>

# Subscriptions

Types:

```python
from tecmie.types import SubscriptionDto
```

Methods:

- <code title="post /subscription">client.subscriptions.<a href="./src/tecmie/resources/subscriptions/subscriptions.py">create</a>(\*\*<a href="src/tecmie/types/subscription_create_params.py">params</a>) -> <a href="./src/tecmie/types/subscription_dto.py">SubscriptionDto</a></code>
- <code title="get /subscription/{id}">client.subscriptions.<a href="./src/tecmie/resources/subscriptions/subscriptions.py">retrieve</a>(id, \*\*<a href="src/tecmie/types/subscription_retrieve_params.py">params</a>) -> <a href="./src/tecmie/types/subscription_dto.py">SubscriptionDto</a></code>
- <code title="patch /subscription/{id}">client.subscriptions.<a href="./src/tecmie/resources/subscriptions/subscriptions.py">update</a>(path_id, \*\*<a href="src/tecmie/types/subscription_update_params.py">params</a>) -> <a href="./src/tecmie/types/subscription_dto.py">SubscriptionDto</a></code>

## Change

Methods:

- <code title="patch /subscription/change">client.subscriptions.change.<a href="./src/tecmie/resources/subscriptions/change.py">update</a>(path_id, \*\*<a href="src/tecmie/types/subscriptions/change_update_params.py">params</a>) -> <a href="./src/tecmie/types/subscription_dto.py">SubscriptionDto</a></code>

# Contacts

Types:

```python
from tecmie.types import (
    PaginatedContactDto,
    ReadContactDto,
    ContactListResponse,
    ContactDeleteResponse,
)
```

Methods:

- <code title="post /contacts">client.contacts.<a href="./src/tecmie/resources/contacts.py">create</a>(\*\*<a href="src/tecmie/types/contact_create_params.py">params</a>) -> <a href="./src/tecmie/types/read_contact_dto.py">ReadContactDto</a></code>
- <code title="get /contacts/{id}">client.contacts.<a href="./src/tecmie/resources/contacts.py">retrieve</a>(id, \*\*<a href="src/tecmie/types/contact_retrieve_params.py">params</a>) -> <a href="./src/tecmie/types/read_contact_dto.py">ReadContactDto</a></code>
- <code title="patch /contacts/{id}">client.contacts.<a href="./src/tecmie/resources/contacts.py">update</a>(id, \*\*<a href="src/tecmie/types/contact_update_params.py">params</a>) -> <a href="./src/tecmie/types/read_contact_dto.py">ReadContactDto</a></code>
- <code title="get /contacts">client.contacts.<a href="./src/tecmie/resources/contacts.py">list</a>(\*\*<a href="src/tecmie/types/contact_list_params.py">params</a>) -> <a href="./src/tecmie/types/contact_list_response.py">ContactListResponse</a></code>
- <code title="delete /contacts/{id}">client.contacts.<a href="./src/tecmie/resources/contacts.py">delete</a>(id) -> <a href="./src/tecmie/types/contact_delete_response.py">object</a></code>

# ContactGroup

Types:

```python
from tecmie.types import (
    PaginatedContactGroupDto,
    ReadContactGroupDto,
    ContactGroupListResponse,
    ContactGroupDeleteResponse,
)
```

Methods:

- <code title="post /contact_group">client.contact_group.<a href="./src/tecmie/resources/contact_group.py">create</a>(\*\*<a href="src/tecmie/types/contact_group_create_params.py">params</a>) -> <a href="./src/tecmie/types/read_contact_group_dto.py">ReadContactGroupDto</a></code>
- <code title="get /contact_group/{id}">client.contact_group.<a href="./src/tecmie/resources/contact_group.py">retrieve</a>(id, \*\*<a href="src/tecmie/types/contact_group_retrieve_params.py">params</a>) -> <a href="./src/tecmie/types/read_contact_group_dto.py">ReadContactGroupDto</a></code>
- <code title="patch /contact_group/{id}">client.contact_group.<a href="./src/tecmie/resources/contact_group.py">update</a>(id, \*\*<a href="src/tecmie/types/contact_group_update_params.py">params</a>) -> <a href="./src/tecmie/types/read_contact_group_dto.py">ReadContactGroupDto</a></code>
- <code title="get /contact_group">client.contact_group.<a href="./src/tecmie/resources/contact_group.py">list</a>(\*\*<a href="src/tecmie/types/contact_group_list_params.py">params</a>) -> <a href="./src/tecmie/types/contact_group_list_response.py">ContactGroupListResponse</a></code>
- <code title="delete /contact_group/{id}">client.contact_group.<a href="./src/tecmie/resources/contact_group.py">delete</a>(id) -> <a href="./src/tecmie/types/contact_group_delete_response.py">object</a></code>

# Mailbox

Types:

```python
from tecmie.types import (
    PaginatedPipelineDto,
    ReadPipelineDto,
    MailboxListResponse,
    MailboxDeleteResponse,
)
```

Methods:

- <code title="post /mailbox">client.mailbox.<a href="./src/tecmie/resources/mailbox/mailbox.py">create</a>(\*\*<a href="src/tecmie/types/mailbox_create_params.py">params</a>) -> <a href="./src/tecmie/types/read_pipeline_dto.py">ReadPipelineDto</a></code>
- <code title="get /mailbox/{id}">client.mailbox.<a href="./src/tecmie/resources/mailbox/mailbox.py">retrieve</a>(id, \*\*<a href="src/tecmie/types/mailbox_retrieve_params.py">params</a>) -> <a href="./src/tecmie/types/read_pipeline_dto.py">ReadPipelineDto</a></code>
- <code title="patch /mailbox/{id}">client.mailbox.<a href="./src/tecmie/resources/mailbox/mailbox.py">update</a>(id) -> <a href="./src/tecmie/types/read_pipeline_dto.py">ReadPipelineDto</a></code>
- <code title="get /mailbox">client.mailbox.<a href="./src/tecmie/resources/mailbox/mailbox.py">list</a>(\*\*<a href="src/tecmie/types/mailbox_list_params.py">params</a>) -> <a href="./src/tecmie/types/mailbox_list_response.py">MailboxListResponse</a></code>
- <code title="delete /mailbox/{id}">client.mailbox.<a href="./src/tecmie/resources/mailbox/mailbox.py">delete</a>(id) -> <a href="./src/tecmie/types/mailbox_delete_response.py">object</a></code>
- <code title="post /mailbox/availability">client.mailbox.<a href="./src/tecmie/resources/mailbox/mailbox.py">check_availability</a>(\*\*<a href="src/tecmie/types/mailbox_check_availability_params.py">params</a>) -> None</code>

## Registry

Types:

```python
from tecmie.types.mailbox import MailboxRegistryQueryDto, PaginatedMailboxRegistry
```

Methods:

- <code title="get /mailbox/{id}/registry">client.mailbox.registry.<a href="./src/tecmie/resources/mailbox/registry/registry.py">retrieve</a>(id, \*\*<a href="src/tecmie/types/mailbox/registry_retrieve_params.py">params</a>) -> <a href="./src/tecmie/types/mailbox/paginated_mailbox_registry.py">PaginatedMailboxRegistry</a></code>

### Action

Types:

```python
from tecmie.types.mailbox.registry import ActionCreateResponse
```

Methods:

- <code title="post /mailbox/{id}/registry/action">client.mailbox.registry.action.<a href="./src/tecmie/resources/mailbox/registry/action.py">create</a>(id, \*\*<a href="src/tecmie/types/mailbox/registry/action_create_params.py">params</a>) -> <a href="./src/tecmie/types/mailbox/registry/action_create_response.py">ActionCreateResponse</a></code>
- <code title="get /mailbox/{id}/registry/action">client.mailbox.registry.action.<a href="./src/tecmie/resources/mailbox/registry/action.py">retrieve</a>(id, \*\*<a href="src/tecmie/types/mailbox/registry/action_retrieve_params.py">params</a>) -> <a href="./src/tecmie/types/mailbox/paginated_mailbox_registry.py">PaginatedMailboxRegistry</a></code>

### Resource

Types:

```python
from tecmie.types.mailbox.registry import ResourceCreateResponse
```

Methods:

- <code title="post /mailbox/{id}/registry/resource">client.mailbox.registry.resource.<a href="./src/tecmie/resources/mailbox/registry/resource.py">create</a>(id, \*\*<a href="src/tecmie/types/mailbox/registry/resource_create_params.py">params</a>) -> <a href="./src/tecmie/types/mailbox/registry/resource_create_response.py">ResourceCreateResponse</a></code>
- <code title="get /mailbox/{id}/registry/resource">client.mailbox.registry.resource.<a href="./src/tecmie/resources/mailbox/registry/resource.py">retrieve</a>(id, \*\*<a href="src/tecmie/types/mailbox/registry/resource_retrieve_params.py">params</a>) -> <a href="./src/tecmie/types/mailbox/paginated_mailbox_registry.py">PaginatedMailboxRegistry</a></code>

## Stream

Types:

```python
from tecmie.types.mailbox import (
    QueryStreamDto,
    StreamCreateResponse,
    StreamRetrieveResponse,
)
```

Methods:

- <code title="post /mailbox/{id}/stream/{slug}">client.mailbox.stream.<a href="./src/tecmie/resources/mailbox/stream/stream.py">create</a>(id, slug, \*\*<a href="src/tecmie/types/mailbox/stream_create_params.py">params</a>) -> <a href="./src/tecmie/types/mailbox/stream_create_response.py">StreamCreateResponse</a></code>
- <code title="get /mailbox/{id}/stream/{slug}">client.mailbox.stream.<a href="./src/tecmie/resources/mailbox/stream/stream.py">retrieve</a>(id, slug) -> <a href="./src/tecmie/types/mailbox/stream_retrieve_response.py">StreamRetrieveResponse</a></code>

### Registry

Types:

```python
from tecmie.types.mailbox.stream import StreamRegistryQueryDto
```

Methods:

- <code title="get /mailbox/{id}/stream/{slug}/registry">client.mailbox.stream.registry.<a href="./src/tecmie/resources/mailbox/stream/registry/registry.py">retrieve</a>(id, slug, \*\*<a href="src/tecmie/types/mailbox/stream/registry_retrieve_params.py">params</a>) -> <a href="./src/tecmie/types/mailbox/stream/registry/paginated_stream_registry.py">PaginatedStreamRegistry</a></code>

#### Action

Types:

```python
from tecmie.types.mailbox.stream.registry import OneStreamRegistryAction
```

Methods:

- <code title="post /mailbox/{id}/stream/{slug}/registry/action">client.mailbox.stream.registry.action.<a href="./src/tecmie/resources/mailbox/stream/registry/action.py">create</a>(id, slug, \*\*<a href="src/tecmie/types/mailbox/stream/registry/action_create_params.py">params</a>) -> <a href="./src/tecmie/types/mailbox/stream/registry/one_stream_registry_action.py">OneStreamRegistryAction</a></code>
- <code title="get /mailbox/{id}/stream/{slug}/registry/action">client.mailbox.stream.registry.action.<a href="./src/tecmie/resources/mailbox/stream/registry/action.py">retrieve</a>(id, slug, \*\*<a href="src/tecmie/types/mailbox/stream/registry/action_retrieve_params.py">params</a>) -> <a href="./src/tecmie/types/mailbox/stream/registry/paginated_stream_registry.py">PaginatedStreamRegistry</a></code>

#### Resource

Types:

```python
from tecmie.types.mailbox.stream.registry import PaginatedStreamRegistry
```

Methods:

- <code title="post /mailbox/{id}/stream/{slug}/registry/resource">client.mailbox.stream.registry.resource.<a href="./src/tecmie/resources/mailbox/stream/registry/resource.py">create</a>(id, slug, \*\*<a href="src/tecmie/types/mailbox/stream/registry/resource_create_params.py">params</a>) -> <a href="./src/tecmie/types/mailbox/stream/registry/one_stream_registry_action.py">OneStreamRegistryAction</a></code>
- <code title="get /mailbox/{id}/stream/{slug}/registry/resource">client.mailbox.stream.registry.resource.<a href="./src/tecmie/resources/mailbox/stream/registry/resource.py">retrieve</a>(id, slug, \*\*<a href="src/tecmie/types/mailbox/stream/registry/resource_retrieve_params.py">params</a>) -> <a href="./src/tecmie/types/mailbox/stream/registry/paginated_stream_registry.py">PaginatedStreamRegistry</a></code>

# Inbound

## Mail

Methods:

- <code title="post /inbound/mail">client.inbound.mail.<a href="./src/tecmie/resources/inbound/mail.py">create</a>(\*\*<a href="src/tecmie/types/inbound/mail_create_params.py">params</a>) -> None</code>
