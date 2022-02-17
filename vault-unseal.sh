#!/bin/bash
#
# Unseal Vault
#

PASS_FILE='/etc/vault/seal.token'

if $(vault status | grep Sealed | awk '{print $2}'); then
  vault operator unseal $(cat ${PASS_FILE})
fi

if $(vault status | grep Sealed | awk '{print $2}'); then
  echo "An error occured, the Vault is still sealed."
fi
