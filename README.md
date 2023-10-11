# Apple Store Notifier

Checks Apple Store for availability and sends a message to Discord.

Before running the script, run `cp config.toml.template config.toml` and set up the config file with your values. `location` and `model` are required. `discord_webhook` is required if you want to send a message to Discord. Without it, you'll only get output on stdout.

If the script outputs nothing, this means there is no availability. Output is suppressed to avoid spamming with notifications.

## Model number reference

| Phone | Color | Size | Model number |
|--|--|--|--|
iPhone 15 Pro | Black Titanium | 128GB | MTQM3LL/A |
iPhone 15 Pro | Black Titanium | 256GB | MTQR3LL/A |
iPhone 15 Pro | Black Titanium | 512GB | MTQW3LL/A |
iPhone 15 Pro | Black Titanium | 1TB | MTU13LL/A |
iPhone 15 Pro | Natural Titanium | 128GB | MTQP3LL/A |
iPhone 15 Pro | Natural Titanium | 256GB | MTQU3LL/A |
iPhone 15 Pro | Natural Titanium | 512GB | MTQY3LL/A |
iPhone 15 Pro | Natural Titanium | 1TB | MTU53LL/A |
iPhone 15 Pro | Blue Titanium | 128GB | MTQQ3LL/A |
iPhone 15 Pro | Blue Titanium | 256GB | MTQV3LL/A |
iPhone 15 Pro | Blue Titanium | 512GB | MTU03LL/A |
iPhone 15 Pro | Blue Titanium | 1TB | MTU63LL/A |
iPhone 15 Pro | White Titanium | 128GB | MTQN3LL/A |
iPhone 15 Pro | White Titanium | 256GB | MTQT3LL/A |
iPhone 15 Pro | White Titanium | 512GB | MTQX3LL/A |
iPhone 15 Pro | White Titanium | 1TB | MTU43LL/A |
