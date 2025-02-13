<script lang="ts">
    import { Anthropic } from "@anthropic-ai/sdk";  // Ensure correct import
    import { onMount } from "svelte";
    import { writable } from "svelte/store";
    
    let item1 = writable("");
    let item2 = writable("");
    let API = writable(""); // Declare API as a writable store
    let msg = writable(""); // Declare msg as a writable store

    let client: Anthropic | null = null;

    onMount(async () => {
        // Initialize client with empty API key
        client = new Anthropic({ apiKey: $API });
    });

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
</script>


<h1 class="text-6xl">INFINITE GAME</h1>
<div class="flex flex-col gap-2.5 w-1/4">
    <input class="border" bind:value={$item1} placeholder="Item 1"> 
    <input class="border" bind:value={$item2} placeholder="Item 2">
    <input class="border" bind:value={$API} placeholder="API key">
    <button onclick={coolthing}>Submit</button>
</div>
<p>"{$msg}"</p>