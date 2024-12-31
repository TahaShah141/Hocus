import { useState } from 'react';
import { Dropzone } from './components/Dropzone'
import { Graph } from './components/Graph';

function App() {

  const [json, setJSON] = useState(null);

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-neutral-900 text-neutral-100 p-4 gap-2">
      <h1 className="text-4xl font-bold text-neutral-100">Graph Visualizer</h1>
      {!json && <div className='max-w-3xl w-full'>
        <Dropzone setJSON={setJSON}/>
      </div>}
      {json && <Graph json={json}/>}
      <button className='p-2 rounded-md bg-red-700 border-black border-2' onClick={() => setJSON(null)}>Clear Graph</button>
    </div>
  )
}

export default App
