# Links

[GSM verified Model names](http://storage.googleapis.com/play_public/supported_devices.csv)

[Build numbers and Google devices](https://source.android.com/setup/start/build-numbers)

[UA formats](https://developers.whatismybrowser.com/useragents/)

[Android languages](https://android.googlesource.com/platform/build/+/refs/heads/master/target/product/languages_default.mk)

[Chrome versions](https://en.wikipedia.org/wiki/Google_Chrome_version_history)

[Firefox versions](https://en.wikipedia.org/wiki/Firefox_version_history)

# Formats

android version x.y(.z) .z exists even if zero since O

chrome version x.0.y.z where y is incr

firefox format probably since 17.0.1
> Reverted user agent change causing some website incompatibilities.

## Android Browser (KK and below)

### ICS and above

```
Mozilla/5.0 (Linux; U; Android <android version in x.y(.z)>; <language, dash and lowercase>; <model name> Build/<short build id>) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30
```

### GB & FR

webkit version differs

```
Mozilla/5.0 (Linux; U; Android <android version in x.y(.z)>; <language, dash and lowercase>; <model name> Build/<short build id>) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Safari/533.1
```

## Android Chrome

```
Mozilla/5.0 (Linux; Android <android version in x.y(.z)>; <model name> <(Build/<short build id>)>) AppleWebKit/<webkit/blink version> (KHTML, like Gecko) Chrome/<chrome version> Mobile Safari/<webkit/blink version>
```

## Android Firefox

```
Mozilla/5.0 (Android <android version in x.y(.z)>; Mobile; rv:<firefox version>) Gecko/<firefox version> Firefox/<firefox version>
```

## Linux Chrome

arch: `x86_64, i686`

```
Mozilla/5.0 (X11; Linux <arch>) AppleWebKit/<webkit> (KHTML, like Gecko) Chrome/<chrome> Safari/<webkit>
```

## Linux Firefox

X11 even if on wayland

```
Mozilla/5.0 (X11; <(Ubuntu/Fedora; )>Linux <arch>; rv:<firefox version>) Gecko/20100101 Firefox/<firefox version>
```

## Windows Chrome

64bit: `; Win64; x64`(since 53), `; WOW64`

no xp and vista since 50

```
Mozilla/5.0 (Windows NT <NT ver><(64bit)>) AppleWebKit/<webkit> (KHTML, like Gecko) Chrome/<chrome> Safari/<webkit>
```

## Windows Firefox

64bit: `; Win64; x64`(since 60), `; WOW64`

no xp and vista since 53

```
Mozilla/5.0 (Windows NT <NT ver><64bit>; rv:<firefox version>) Gecko/20100101 Firefox/<firefox version>
```

## Windows IE 6,7

6: xp initial (NT 5.1)
7: vista initial (NT 6.0)

```
Mozilla/4.0 (compatible; MSIE <IE ver>; Windows NT <NT ver><installed .NET>)
```

## Windows IE 8

8: 7 initial (NT 6.1)

```
Mozilla/4.0 (compatible; MSIE <IE ver>; Windows NT <NT ver>; <(WOW64; )>Trident/4.0<installed .NET>)
```

## Windows IE 9

```
Mozilla/5.0 (compatible; MSIE <IE ver>; Windows NT <NT ver>; <(WOW64; )>Trident/5.0<installed .NET>)
```

## Windows IE 10

10: 8 initial (NT 6.2)

```
Mozilla/5.0 (compatible; MSIE <IE ver>; Windows NT <NT ver>; <(WOW64; )>Trident/6.0)
```

## Windows IE 11

10: 8.1 initial (NT 6.3)

```
Mozilla/5.0 (compatible; MSIE <IE ver>; Windows NT <NT ver>; <(WOW64; )>Trident/7.0; rv:11.0) like Gecko
```

## Edge

10 (NT 10.0) only before chromium-based

```
Mozilla/5.0 (Windows NT 10.0<(; Win64; x64)>) AppleWebKit/<webkit> (KHTML, like Gecko) Chrome/<chrome> Safari/<webkit> Edge/<EdgeHTML>
```

## OS X Chrome

os x verion in `x_y_z`

```
Mozilla/5.0 (Macintosh; Intel Mac OS X <os x version>) AppleWebKit/<webkit> (KHTML, like Gecko) Chrome/<chrome> Safari/<webkit>
```

## OS X Firefox

```
Mozilla/5.0 (Macintosh; Intel Mac OS X <version in x.y>; rv:<firefox version>) Gecko/20100101 Firefox/<firefox version>
```

# Data generation

## Chrome versions list (data/chrome.csv)

Copy [Chrome versions](https://en.wikipedia.org/wiki/Google_Chrome_version_history) html, strip to contain only main `<table>`, import into google sheets, delete columns except major version and layout version, delete header and future versions rows, delete 'Webkit' and 'Blink', export as csv and manually fill or fix layout engine column.
