<script lang='ts' context="module">

 const wordLogKey: string = "riffOffWordLogKey";
 
   export function recordWordToStorage(word: string, maxWordNum: number) {
        let wordArray = getWordsFromStorage()
        if (wordArray.length >= maxWordNum){
            wordArray.shift()
        }
        wordArray.push(word)
        localStorage.setItem(wordLogKey, JSON.stringify(wordArray))
    }
    
   export function getWordsFromStorage(): string[] {
       let wordArray = JSON.parse(localStorage.getItem(wordLogKey) || "[]")
       return wordArray
    }
</script>