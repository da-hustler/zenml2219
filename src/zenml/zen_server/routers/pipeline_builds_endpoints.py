#  Copyright (c) ZenML GmbH 2022. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.
"""Endpoint definitions for builds."""

from typing import Optional, Union
from uuid import UUID

from fastapi import APIRouter, Depends, Security

from zenml.constants import API, PIPELINE_BUILDS, VERSION_1
from zenml.models import (
    Page,
    PipelineBuildFilter,
    PipelineBuildRequest,
    PipelineBuildResponse,
)
from zenml.zen_server.auth import AuthContext, authorize
from zenml.zen_server.exceptions import error_response
from zenml.zen_server.rbac.endpoint_utils import (
    verify_permissions_and_create_entity,
    verify_permissions_and_delete_entity,
    verify_permissions_and_get_entity,
    verify_permissions_and_list_entities,
)
from zenml.zen_server.rbac.models import ResourceType
from zenml.zen_server.routers.workspaces_endpoints import (
    router as workspace_router,
)
from zenml.zen_server.utils import (
    handle_exceptions,
    make_dependable,
    zen_store,
)

router = APIRouter(
    prefix=API + VERSION_1 + PIPELINE_BUILDS,
    tags=["builds"],
    responses={401: error_response, 403: error_response},
)


@router.post(
    "",
    response_model=PipelineBuildResponse,
    responses={401: error_response, 409: error_response, 422: error_response},
)
@workspace_router.post(
    "/{workspace_name_or_id}" + PIPELINE_BUILDS,
    response_model=PipelineBuildResponse,
    responses={401: error_response, 409: error_response, 422: error_response},
)
@handle_exceptions
def create_build(
    build: PipelineBuildRequest,
    workspace_name_or_id: Optional[Union[str, UUID]] = None,
    _: AuthContext = Security(authorize),
) -> PipelineBuildResponse:
    """Creates a build, optionally in a specific workspace.

    Args:
        build: Build to create.
        workspace_name_or_id: Optional name or ID of the workspace.

    Returns:
        The created build.
    """
    if workspace_name_or_id:
        workspace = zen_store().get_workspace(workspace_name_or_id)
        build.workspace = workspace.id

    return verify_permissions_and_create_entity(
        request_model=build,
        resource_type=ResourceType.PIPELINE_BUILD,
        create_method=zen_store().create_build,
    )


@router.get(
    "",
    response_model=Page[PipelineBuildResponse],
    responses={401: error_response, 404: error_response, 422: error_response},
)
@workspace_router.get(
    "/{workspace_name_or_id}" + PIPELINE_BUILDS,
    response_model=Page[PipelineBuildResponse],
    responses={401: error_response, 404: error_response, 422: error_response},
)
@handle_exceptions
def list_builds(
    build_filter_model: PipelineBuildFilter = Depends(
        make_dependable(PipelineBuildFilter)
    ),
    workspace_name_or_id: Optional[Union[str, UUID]] = None,
    hydrate: bool = False,
    _: AuthContext = Security(authorize),
) -> Page[PipelineBuildResponse]:
    """Gets a list of builds, optionally filtered by workspace.

    Args:
        build_filter_model: Filter model used for pagination, sorting,
            filtering.
        workspace_name_or_id: Optional name or ID of the workspace to filter by.
        hydrate: Flag deciding whether to hydrate the output model(s)
            by including metadata fields in the response.

    Returns:
        List of build objects matching the filter criteria.
    """
    if workspace_name_or_id:
        workspace = zen_store().get_workspace(workspace_name_or_id)
        build_filter_model.set_scope_workspace(workspace.id)

    return verify_permissions_and_list_entities(
        filter_model=build_filter_model,
        resource_type=ResourceType.PIPELINE_BUILD,
        list_method=zen_store().list_builds,
        hydrate=hydrate,
    )


@router.get(
    "/{build_id}",
    response_model=PipelineBuildResponse,
    responses={401: error_response, 404: error_response, 422: error_response},
)
@handle_exceptions
def get_build(
    build_id: UUID,
    hydrate: bool = True,
    _: AuthContext = Security(authorize),
) -> PipelineBuildResponse:
    """Gets a specific build using its unique id.

    Args:
        build_id: ID of the build to get.
        hydrate: Flag deciding whether to hydrate the output model(s)
            by including metadata fields in the response.

    Returns:
        A specific build object.
    """
    return verify_permissions_and_get_entity(
        id=build_id, get_method=zen_store().get_build, hydrate=hydrate
    )


@router.delete(
    "/{build_id}",
    responses={401: error_response, 404: error_response, 422: error_response},
)
@handle_exceptions
def delete_build(
    build_id: UUID,
    _: AuthContext = Security(authorize),
) -> None:
    """Deletes a specific build.

    Args:
        build_id: ID of the build to delete.
    """
    verify_permissions_and_delete_entity(
        id=build_id,
        get_method=zen_store().get_build,
        delete_method=zen_store().delete_build,
    )
