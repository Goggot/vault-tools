#!/usr/bin/env python
#
# Dump all k/v engine data in json
# Require to login with root token
#

import json
import subprocess

def loop_in_path(parent, fullpath):
  json_parent = {f"{parent}": {}}
  output = subprocess.run(["vault", "kv", "list", "-format", "json", f"{fullpath}"], text=True, capture_output=True)
  slist = json.loads(output.stdout.strip())
  for secret in slist:
    if secret.endswith('/'):
      json_parent[parent].update(loop_in_path(secret, f"{fullpath}{secret}"))
    else:
      item = subprocess.run(["vault", "kv", "get", "-format", "json", f"{fullpath}{secret}"], text=True, capture_output=True)
      jitem = json.loads(item.stdout.strip())
      json_parent[parent].update({secret: {'data': jitem['data']['data'], 'metadata': jitem['data']['metadata']['custom_metadata']}})

  return json_parent

# MAIN
subprocess.run(["vault", "login"], stdout=subprocess.DEVNULL)
output = subprocess.run(["vault", "secrets", "list" ,"-format" ,"json"], text=True, capture_output=True)
engine_list = json.loads(output.stdout.strip())
final_json = {}

for engine in engine_list:
  if engine_list[engine]['type'] == 'kv':
    final_json.update(loop_in_path(engine, engine))

print(final_json)
