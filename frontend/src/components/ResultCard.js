import React from "react";

const ResultCard = ({ result }) => {
  if (!result) return null;

  return (
    <div className="w-full max-w-3xl bg-gray-800 p-4 rounded-lg mt-4 border border-gray-700">
      <h3 className="text-xl font-semibold text-green-400">Hasil Pencarian:</h3>
      <pre className="bg-black p-3 mt-2 rounded overflow-x-auto text-green-300 text-sm">
        {result}
      </pre>
    </div>
  );
};

export default ResultCard;
