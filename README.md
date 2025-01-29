# DSChaosMod

## What is this?

DSChaosMod is a repository for adding a sort of 'Twitch integration' to Dark Souls, wherein viewers can vote in a streamer's chat to interact with their gameplay.

Visit the [Wiki](https://github.com/milkytoasto/DSChaosMod/wiki) for specific details on contributing to this application.

## Installing

Note: This repository uses Python v3.9 and may not be compatible with later Python versions.

1. Clone the repository
2. Go into the project root directory with `cd DSChaosMod`
3. `pip install poetry` to get the Poetry dependency
4. `poetry install` to get both base and dev dependencies
5. `poetry run pre-commit install` to install the pre-commit hooks
6. `poetry run pre-commit run -a` to run the pre-commit hooks. This will make sure they are operating as expected.

And that should be all you need to get started on development. There is more planned with the mod as it is still in the early stages, so this is subject to change.

At this time I would recommend running `git update-index --assume-unchanged .\TwitchVotingServer\config\config.ini` to prevent committing any secrets you may store in there.

## Usage

Currently there is a GUI server that can be initiated by running the `server.py` file. 

In the TwitchVotingOverlay directory you will find an HTML file that can be viewed in your browser or added to OBS as a browser source that will receive messages from the websocket server on port 7890. The websocket server itself now runs by default when the server file is ran, and listens to port 7890. If you desire for some reason to change this, it will need to be changed in the corresponding HTML file as well.

`Connect to Twitch` will initialize the tasks to connect to Twitch as well as the actual voting handler.

`Disconnect` will end the tasks and disconnect from Twitch.

`Start` will initiate the voting handler and Twitch bot.

`Pause` will pause the voting state so that it may be resumed again with `Start`.

`Stop` will stop the voting handler as well as the Twitch bot.
