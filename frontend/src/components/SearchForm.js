import React from "react";

const SearchForm = ({ type, setType, query, setQuery, handleSearch, loading }) => {
  return (
    <div className="flex flex-col items-center mt-6">
      <div className="flex gap-4 mb-4">
        <select
          value={type}
          onChange={(e) => setType(e.target.value)}
          className="p-2 bg-gray-800 border border-gray-600 rounded"
        >
          <option value="username">Username</option>
          <option value="email">Email</option>
          <option value="domain">Domain</option>
        </select>
        <input
          type="text"
          placeholder="Masukkan data..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="p-2 bg-gray-800 border border-gray-600 rounded text-white placeholder-gray-400"
        />
        <button
          onClick={handleSearch}
          disabled={loading}
          className="p-2 bg-blue-600 hover:bg-blue-500 text-white rounded"
        >
          {loading ? "Mencari..." : "Cari"}
        </button>
      </div>
    </div>
  );
};

export default SearchForm;
