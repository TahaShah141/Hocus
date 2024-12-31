import { useState, useEffect, } from 'react';

function Node({node}) {
  const [color, setColor] = useState('');

  // console.log(node)
  useEffect(() => {
    // console.log("Checking nodeRef :", nodeRef.current);
    // Set color based on type
    if (node.type === 'start' || node.type === 'end') {
      setColor('bg-red-500');
    } else if (node.type === 'deadend') {
      setColor('bg-gray-800');
    }

  }, [node]);

  return (
    <>
      <div
        className={`absolute w-[35px] h-[35px] ${color} border border-black rounded-full`}
        style={{
          top: `${node.absoluteY}px`,
          left: `${node.absoluteX}px`,
        }}
      >
        <p>{'hex' + node.hexName}</p>
        <p>{node.type}</p>
        <p>{node.dimensions}</p>
      </div>
    </>
  );
}

export default Node;
