# Unity

Unity has 2 scripting backends:
Mono
Il2CPP

Mono = Assembly-CSharp.dll with C# Code (Just In Time Compilation)
Il2CPP = GameAssembly.dll with pre-compiled code

on Il2CPP a function/method will have a fixed offset like any other native game.

PE = Portable Executable:
The PE format is a data structure that encapsulates the information necessary for the Windows OS loader to manage the wrapped executable code, so Assembly-CSharp and GameAssembly.dll are both PE Files.
In a .NET/Mono executable, the PE code section contains a stub that invokes the CLR virtual machine startup entry.

Ref: https://fearlessrevolution.com/viewtopic.php?t=14367

## Assets

### UnityPack

```
pip install unitypack
```

The above command may fail with `<malloc.h> not found` on Mac OSX when
installing `decrunch` dependency. In this case, you need to install `decrunch`
manually.

```
git clone --depth=1 https://github.com/HearthSim/decrunch.git
cd decrunch

cat <<EOF | git apply -
diff --git a/crunch/crn_decomp.h b/crunch/crn_decomp.h
index 381051e..edc4d95 100644
--- a/crunch/crn_decomp.h
+++ b/crunch/crn_decomp.h
@@ -341,6 +341,8 @@ const unsigned int cCRNHeaderMinSize = 62U;
 #include <stdlib.h>
 #ifdef WIN32
 #include <memory.h>
+#elif defined __APPLE__
+#include <malloc/malloc.h>
 #else
 #include <malloc.h>
 #endif
EOF

pip install Cython
python ./setup.py install
```

## Resources

* https://phepe.github.io/2019/02/20/Unity3d/DisUnity/
* https://github.com/Perfare/AssetStudio
* https://github.com/ata4/disunity
* https://github.com/HearthSim/UnityPack
* https://github.com/K0lb3/UnityPy#example
* https://www.unknowncheats.me/forum/unity/285864-beginners-guide-hacking-unity-games.html
* https://github.com/imadr/Unity-game-hacking#extracting-assets
* https://github.com/kmichel/zizany
* https://github.com/mafaca/UtinyRipper
* https://github.com/Unity-Technologies/AssetBundles-Browser
* http://www.alanzucconi.com/2015/09/02/a-practical-tutorial-to-hack-and-protect-unity-games/
* https://github.com/socialpoint-labs/unity-yaml-parser
