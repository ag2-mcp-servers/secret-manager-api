# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T02:48:11+00:00



import argparse
import json
import os
from typing import *
from typing import Optional

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import BaseSecurity, UnsuportedSecurityStub
from fastapi import Query

from models import (
    AccessSecretVersionResponse,
    AddSecretVersionRequest,
    Alt,
    DestroySecretVersionRequest,
    DisableSecretVersionRequest,
    Empty,
    EnableSecretVersionRequest,
    FieldXgafv,
    ListLocationsResponse,
    ListSecretsResponse,
    ListSecretVersionsResponse,
    Policy,
    Secret,
    SecretVersion,
    SetIamPolicyRequest,
    TestIamPermissionsRequest,
    TestIamPermissionsResponse,
)

app = MCPProxy(
    contact={'name': 'Google', 'url': 'https://google.com', 'x-twitter': 'youtube'},
    description='Stores sensitive data such as API keys, passwords, and certificates. Provides convenience while improving security. ',
    license={
        'name': 'Creative Commons Attribution 3.0',
        'url': 'http://creativecommons.org/licenses/by/3.0/',
    },
    termsOfService='https://developers.google.com/terms/',
    title='Secret Manager API',
    version='v1beta1',
    servers=[{'url': 'https://secretmanager.googleapis.com/'}],
)


@app.delete(
    '/v1beta1/{name}',
    description=""" Deletes a Secret. """,
    tags=['secret_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def secretmanager_projects_secrets_delete(
    name: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1beta1/{name}',
    description=""" Gets metadata for a SecretVersion. `projects/*/secrets/*/versions/latest` is an alias to the `latest` SecretVersion. """,
    tags=[
        'secret_management',
        'secret_version_handling',
        'secret_iam_policy_actions',
        'secret_storage_location_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def secretmanager_projects_secrets_versions_get(
    name: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.patch(
    '/v1beta1/{name}',
    description=""" Updates metadata of an existing Secret. """,
    tags=['secret_management', 'secret_version_handling'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def secretmanager_projects_secrets_patch(
    name: str,
    update_mask: Optional[str] = Query(None, alias='updateMask'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: Secret = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1beta1/{name}/locations',
    description=""" Lists information about the supported locations for this service. """,
    tags=['secret_management', 'secret_version_handling'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def secretmanager_projects_locations_list(
    name: str,
    filter: Optional[str] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1beta1/{name}:access',
    description=""" Accesses a SecretVersion. This call returns the secret data. `projects/*/secrets/*/versions/latest` is an alias to the `latest` SecretVersion. """,
    tags=[
        'secret_management',
        'secret_version_handling',
        'secret_iam_policy_actions',
        'secret_storage_location_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def secretmanager_projects_secrets_versions_access(
    name: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1beta1/{name}:destroy',
    description=""" Destroys a SecretVersion. Sets the state of the SecretVersion to DESTROYED and irrevocably destroys the secret data. """,
    tags=['secret_management', 'secret_version_handling'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def secretmanager_projects_secrets_versions_destroy(
    name: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: DestroySecretVersionRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1beta1/{name}:disable',
    description=""" Disables a SecretVersion. Sets the state of the SecretVersion to DISABLED. """,
    tags=['secret_version_handling'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def secretmanager_projects_secrets_versions_disable(
    name: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: DisableSecretVersionRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1beta1/{name}:enable',
    description=""" Enables a SecretVersion. Sets the state of the SecretVersion to ENABLED. """,
    tags=['secret_management', 'secret_version_handling'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def secretmanager_projects_secrets_versions_enable(
    name: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: EnableSecretVersionRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1beta1/{parent}/secrets',
    description=""" Lists Secrets. """,
    tags=['secret_management', 'secret_version_handling'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def secretmanager_projects_secrets_list(
    parent: str,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1beta1/{parent}/secrets',
    description=""" Creates a new Secret containing no SecretVersions. """,
    tags=['secret_management', 'secret_version_handling'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def secretmanager_projects_secrets_create(
    parent: str,
    secret_id: Optional[str] = Query(None, alias='secretId'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: Secret = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1beta1/{parent}/versions',
    description=""" Lists SecretVersions. This call does not return secret data. """,
    tags=[
        'secret_management',
        'secret_version_handling',
        'secret_iam_policy_actions',
        'secret_storage_location_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def secretmanager_projects_secrets_versions_list(
    parent: str,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1beta1/{parent}:addVersion',
    description=""" Creates a new SecretVersion containing secret data and attaches it to an existing Secret. """,
    tags=['secret_management', 'secret_version_handling'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def secretmanager_projects_secrets_add_version(
    parent: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: AddSecretVersionRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1beta1/{resource}:getIamPolicy',
    description=""" Gets the access control policy for a secret. Returns empty policy if the secret exists and does not have a policy set. """,
    tags=['secret_iam_policy_actions'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def secretmanager_projects_secrets_get_iam_policy(
    resource: str,
    options_requested_policy_version: Optional[int] = Query(
        None, alias='options.requestedPolicyVersion'
    ),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1beta1/{resource}:setIamPolicy',
    description=""" Sets the access control policy on the specified secret. Replaces any existing policy. Permissions on SecretVersions are enforced according to the policy set on the associated Secret. """,
    tags=['secret_iam_policy_actions'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def secretmanager_projects_secrets_set_iam_policy(
    resource: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: SetIamPolicyRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1beta1/{resource}:testIamPermissions',
    description=""" Returns permissions that a caller has for the specified secret. If the secret does not exist, this call returns an empty set of permissions, not a NOT_FOUND error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning. """,
    tags=['secret_iam_policy_actions'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def secretmanager_projects_secrets_test_iam_permissions(
    resource: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: TestIamPermissionsRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
