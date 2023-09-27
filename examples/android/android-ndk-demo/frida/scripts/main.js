Java.perform(function() {
  var Activity = Java.use('android.app.Activity');

  var onCreate = Activity.onCreate.overload('android.os.Bundle');
  onCreate.implementation = function(savedInstanceState) {
    console.log('android.app.Activity.onCreate: ', this);
    onCreate.call(this, savedInstanceState);
  };

  var onResume = Activity.onResume;
  onResume.implementation = function() {
    console.log('android.app.Activity.onResume: ', this);
    onResume.call(this);
  };

  var onDestroy = Activity.onDestroy;
  onDestroy.implementation = function() {
    console.log('android.app.Activity.onDestroy: ', this);
    onDestroy.call(this);
  };
});
