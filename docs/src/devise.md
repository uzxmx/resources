# Devise

In `default_middleware_stack.rb` of `railties` gem, it configures rack
middlewares to use `session_store`, which is usually configured in an
initializer file of a rails app. For example:

```
Rails.application.config.session_store :cookie_store, key: "_demo_session"
```

In `devise/rails.rb` of `devise` gem, it configures rack middlewares to use
`Warden::Manager` and save reference for the warden config. And then later in
`devise.rb` it configures warden, e.g. set default strategies for each mapping
(scope).

`devise` uses `to_adapter` method provided by `orm_adapter` gem to identify
whether the model is `ActiveRecord` or some other.

## Strategies

In `devise`, there are `DatabaseAuthenticatable` and `Rememberable` strategy.
Each strategy is checked in registration order to see if it is valid to apply
(by `valid?` method). The `authenticate` method will only be called on a valid
strategy.

`DatabaseAuthenticatable` strategy authenticates by auth params, such as
username and password. So it only works when a sign_in request comes.

`Rememberable` strategy authenticates by using a remember_me cookie. If the
cookie exists, it loads the resource by the value. So this strategy works for
all requests after a user signed in.
