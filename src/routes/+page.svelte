<script lang="ts">
    //import { Anthropic } from "@anthropic-ai/sdk";  // Ensure correct import
    import { onMount } from "svelte";
    import { writable, get } from "svelte/store";
    import OpenAI from "openai";

    let KEY = writable("");
    
    let openai: any;

    let item1 = writable("");
    let item2 = writable("");
    //let API = writable(""); // Declare API as a writable store
    let msg = writable(""); // Declare msg as a writable store

    //let client: Anthropic | null = null;

    /*
    onMount(async () => {
        // Initialize client with empty API key
        client = new Anthropic({ apiKey: $API });
    });
    */

    async function generate(): Promise<string> {
        
        const item1temp = get(item1);
        const item2temp = get(item2);

        if (!openai) {
            console.log("API key is missing");
            return "API key is missing";
        }

        try {
            const response = await openai.chat.completions.create({
                model: "gemini-1.5-flash",
                messages: [
                    { role: "system", content: "Make a new item" },
                    { role: "user", content: `Use ${item1temp} and ${item2temp} to make a new item` }
                ]
            });

            return response.choices[0].message.content;
        } catch (error) {
            console.error("Error with the API:", error);
            return "Error with the API";
        }
        
    }

    /*
    async function coolthing() {
    try {
        if (client) {
            // Update client with new API key
            client = new Anthropic({ apiKey: $API });

            const response = await client.messages.create({
                model: "claude-3-5-sonnet-20241022",
                messages: [
                    { role: "user", content: 'Use $item1 and $item2 to make a new item' },
                    { role: "user", content: 'Use $item1 and $item2 to make a new item' }
                ],
                max_tokens: 8192,
                temperature: 1
            });
        } else {
            console.error("Client is null");
        }
    } catch (error) {
        console.error("Error with the API:", error);
    }
}
    */
</script>


<h1 class="text-6xl">INFINITE GAME</h1>
<div class="flex flex-col gap-2.5 w-1/4">
    <input class="border" bind:value={$item1} placeholder="Item 1"> 
    <input class="border" bind:value={$item2} placeholder="Item 2">
    <!--<input class="border" bind:value={$API} placeholder="API key">-->
    <button onclick={ async () => {
        let message = await generate();
        msg.set(message);
    }}>Submit</button>
</div>
<p>"{$msg}"</p>
<div>
    <input class="border" bind:value={$KEY} placeholder="Key">
    <button onclick={ () => {
        try {
            openai = new OpenAI({ apiKey: $KEY, baseURL: "https://generativelanguage.googleapis.com/v1beta/openai/", dangerouslyAllowBrowser: true });
            console.log("API initialized");
        }
        catch (error) {
            console.error("Error with the API:", error);
        }
    }}
    >Submit Key</button>
</div>