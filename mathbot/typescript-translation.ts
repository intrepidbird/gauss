import { Client, Intents, Message } from 'discord.js';
import { createServer } from 'http';
import * as math from 'mathjs';
import * as fs from 'fs';
import * as express from 'express';
import * as wolfram from 'wolfram-alpha-api';

const client = new Client({ intents: [Intents.FLAGS.Guilds, Intents.FLAGS.GuildMessages] });
const waApi = wolfram.createClient('id');
const app = express();

app.get('/', (req, res) => {
    res.send('[+] Ready');
});

createServer(app).listen(8000);

client.once('ready', () => {
    console.log('[+] Ready');
});

client.on('messageCreate', async (message: Message) => {
    if (!message.content.startsWith('!') || message.author.bot) return;

    const args = message.content.slice(1).trim().split(/ +/);
    const command = args.shift()?.toLowerCase();

    switch (command) {
        case 'flag':
            await message.channel.send('intrepidbird{m47h3mag1c14n}');
            break;
        case 'calculate':
            try {
                const result = math.evaluate(args.join(' '));
                await message.channel.send(result.toString());
            } catch (error) {
                await message.channel.send('Please enter a valid mathematical expression.');
            }
            break;
        case 'factorial':
            const num = parseInt(args[0]);
            if (isNaN(num)) {
                await message.channel.send('Please enter a valid number.');
                return;
            }
            const result = math.factorial(num);
            await message.channel.send(`The factorial of ${num} is: ${result}`);
            break;
        case 'square':
            const num = parseFloat(args[0]);
            if (isNaN(num)) {
                await message.channel.send('Please enter a valid number.');
                return;
            }
            const result = math.square(num);
            await message.channel.send(`The square of ${num} is: ${result}`);
            break;
        case 'factor':
            const num = parseInt(args[0]);
            if (isNaN(num)) {
                await message.channel.send('Please enter a valid number.');
                return;
            }
            const factors = math.divide(math.range(1, num + 1).toArray(), num).filter((n: number) => n % 1 === 0);
            await message.channel.send(`The factors of ${num} are: ${factors}`);
            break;
        default:
            await message.reply(`I didn't understand that command. Try !help.`);
    }
});

client.login('your-token-goes-here');
