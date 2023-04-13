<script lang='ts'>
    import {page} from '$app/stores'
    import { onMount } from 'svelte';
    import * as confetti from 'canvas-confetti'
    import Button from '../../Button.svelte'
    
    const winner: string = $page.url.searchParams.get('winner')
    $: color = winner; 
    
    let isReadyToPlay: string = "invisible";
    
    let myCanvas = document.getElementById('canvas');
    let myConfetti = confetti.create(myCanvas, {
    resize: true,
    useWorker: true
    });
    
    function setConfettiIntervals(delay, repetitions) {
        let confettiBursts: number = 0;
        let intervalID = setInterval(() => {
            console.log(confettiBursts)
            
            myConfetti({
            particleCount: 300,
            spread: 160,
            origin: {
                x: Math.random(),
                y: Math.random() - 0.2,
            },
            });
            
            if (confettiBursts >= repetitions) {
                window.clearInterval(intervalID)
                isReadyToPlay = "visible"
                return
            }
            
            
            
            confettiBursts++
        }, delay);
    }
    
    setConfettiIntervals(1000, 3);
    // onMount(() => {
    //     setConfettiIntervals(1000, 3);
        
    // });
</script>

<canvas id="canvas"></canvas>
<h1 class="font-pacifico text-center text-{color}-400 underline decoration-{color}-400 text-6xl">{winner} wins!</h1>
<a href="/" class="{isReadyToPlay} block text-center font-pacifico w-full my-32 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
  Play Again?
</a>
