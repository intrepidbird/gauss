const Discord = require('discord.js');
const axios = require('axios');
const client = new Discord.Client();

client.on('ready', () => {
    console.log(`Bot is ready as: ${client.user.tag}`);
});

client.on('message', async message => {
    if (message.content.startsWith('!question')) {
        const question = message.content.slice(10);
        const response = await askGpt3(question);
        message.channel.send(response);
    }
});

async function askGpt3(prompt) {
    const data = {
        'prompt': prompt,
        'max_tokens': 60
    };

    const config = {
        headers: {
            'Authorization': `Bearer your-openai-api-key`,
            'Content-Type': 'application/json'
        }
    };

    try {
        const response = await axios.post('https://api.openai.com/v1/engines/davinci-codex/completions', data, config);
        return response.data.choices[0].text.trim();
    } catch (error) {
        console.error(error);
    }
}

client.login('your-discord-bot-token');

// Test Code (beta-release)
