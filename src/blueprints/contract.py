from src.models.deployment import ContractToDeploy
from src.models.invoke import ContractToInvoke
from src.services.contract_deployment import deploy_to_chain_api
from src.services.contract_compilation import compile_contract_api
from src.services.contract_invokation import invoke_contract_api

from flask import Blueprint, request

contract_blueprint = Blueprint(name="contract_blueprint", import_name=__name__)


@contract_blueprint.route('/compile', methods=['POST'])
def compile_contract_blueprint():
    lib_file = request.json["lib_file"]
    return compile_contract_api(lib_file=lib_file)


@ contract_blueprint.route('/deploy', methods=['POST'])
def deploy_to_chain_blueprint():
    contract = ContractToDeploy(
        lib_file=request.json["lib_file"], secret_key=request.json["secret_key"])
    return deploy_to_chain_api(contract)


@ contract_blueprint.route('/invoke', methods=['POST'])
def invoke_contract_api(contract: ContractToInvoke):
    return invoke_contract_api(contract)
