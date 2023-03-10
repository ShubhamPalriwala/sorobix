import subprocess
from src.models.invoke import ContractToInvoke


def prepare_soroban(method: str, contract: ContractToInvoke) -> str:
    base_call = f"soroban contract {method} \
    --id {contract.contract_id} \
    --secret-key {contract.secret_key} \
    --rpc-url https://horizon-futurenet.stellar.cash:443/soroban/rpc \
    --network-passphrase 'Test SDF Future Network ; October 2022' \
    --fn {contract.contract_function} --"

    if len(contract.contract_arguments) > 0:
        updated_call = add_args_in_soroban(
            base_call, contract.contract_arguments)
        return updated_call
    return base_call


def add_args_in_soroban(base_call: str, args: list[str]) -> str:
    for index, arg in enumerate(args):
        if index % 2 == 0:
            base_call += f" --{arg} "
        else:
            base_call += arg
    return base_call


def call_soroban(call_comm: str):
    invoke_contract_proc = subprocess.run(
        [call_comm], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if invoke_contract_proc.stdout != '':
        return {"success": True, "results": invoke_contract_proc.stdout}
    else:
        return {"success": False, "results": invoke_contract_proc.stderr}
