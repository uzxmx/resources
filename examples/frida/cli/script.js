const moduleSymbols = {};
function findSymbolByName(moduleName, symbolName) {
  let symbols = moduleSymbols[moduleName];
  if (!symbols) {
    symbols = Module.enumerateSymbols(moduleName);
    moduleSymbols[moduleName] = symbols;
  }
  return symbols.find(function(e) {
    return e.name === symbolName;
  });
}

Interceptor.attach(Module.findExportByName(null, 'malloc'), {
  onEnter: function (args) {
    console.log("malloc(" + args[0].toInt32() + ")");
  },
  onLeave: function (retval) {
    console.log("-> 0x" + retval.toString(16));
  }
});

Interceptor.attach(Module.findExportByName(null, 'free'), {
  onEnter: function (args) {
    console.log("free(0x" + args[0].toString(16) + ")");
  }
});

Interceptor.attach(Module.findExportByName(null, 'puts'), {
  onEnter: function (args) {
    console.log("puts(" + args[0] + ")");
  }
});

Interceptor.attach(findSymbolByName('main', 'say_hello').address, {
  onEnter: function (args) {
    console.log("say_hello()");
  }
});

Interceptor.attach(findSymbolByName('main', 'static_say_hello').address, {
  onEnter: function (args) {
    console.log("static_say_hello()");
  }
});
