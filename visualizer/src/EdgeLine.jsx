import { useState, useEffect   } from "react";

const EdgeLine = ({ x1, y1, x2, y2,type}) => {
  const offset = 17;
  return (
    <line
      x1={x1+offset}
      y1={y1+offset}
      x2={x2+offset}
      y2={y2+offset }
      stroke="black"
      strokeWidth="2"
      strokeDasharray={type === "dotted" ? "4 2" : "0"}
    />
  );
};

export default EdgeLine