# Unhide Virus Vinyls

```
002469D4 38600001
002469D8 4E800020
```

# Force UnlockSystem::IsDLCUnlock to return true (unlocks everything)

```
000FD234 38600001
001009F8 38600001
```

# Disable Visual Treatment

```
004EB5C4 38600000
```

# Disable Motion Blur

```
004D3408 38000000
```

# Enable IsCollectorsEdition

```
0041550C 38600001
00415510 8122A598
00415514 98690000
```

# Enable Debug Car Customize

```
00666C94 60000000
```

# Force enable MSAA ingame

```
004EBE38 38800001
```

# Force disable MSAA in FrontEnd (menus)

```
004EB9A8 38800000
```

# Restore Unlock All Things cheat (replaces the Autozone vinyl cheat)

- this cheat MUST go into `patches_data.txt`
- enter this cheat code in the main menu to use it: `L1, R1, L1, R1, Left, Right, Left, Right` (it may take a couple of tries, be slow with your inputs)
- once activated, a dialog box with "DEFAULT STRING" will appear

```
10060154 0000003B
10060158 0000003C
1006015C 0000003B
10060160 0000003C
10060164 0000002B
10060168 0000002C
1006016C 0000002B
10060170 0000002C
10060174 00000000
10060178 00000011
1006017C 00000000
10060180 00000000
10060184 00010100
```
