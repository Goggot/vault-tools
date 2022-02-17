# Vault Tools
Various tools and scripts for Hashicorp Vault

## Preparation
- Set the desired environment variables (see [Vault doc](https://www.vaultproject.io/docs/commands))
  ```
  export VAULT_ADDR="https://192.168.0.1:8200"
  export VAULT_SKIP_VERIFY=true
  ```

### Vault Export
- To export every K/V engine datas from Vault:
  ```
  python vault-export.py
  ```

### Vault Unseal
- Enter the seal key in /etc/vault/seal.token
- Run the script:
  ```bash
  ./vault-unseal.sh
  ```
