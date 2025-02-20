import React, { useState } from "react";
import axios from "axios";
import Header from "./components/Header";
import SearchForm from "./components/SearchForm";
import ResultCard from "./components/ResultCard";

function App() {
  const [query, setQuery] = useState("");
  const [type, setType] = useState("username");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    if (!query) {
      alert("Masukkan data untuk mencari!");
      return;
    }
    setLoading(true);
    setResult("");
    try {
      const response = await axios.get(
        `http://127.0.0.1:5000/search/${type}?${type}=${query}`
      );
      console.log("Respon dari backend:", response.data);
      setResult(response.data.result);
    } catch (error) {
      console.error("Error:", error);
      setResult("Terjadi kesalahan atau data tidak ditemukan.");
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white">
      <Header />
      <div className="container mx-auto px-4">
        <SearchForm
          type={type}
          setType={setType}
          query={query}
          setQuery={setQuery}
          handleSearch={handleSearch}
          loading={loading}
        />
        <ResultCard result={result} />
      </div>
    </div>
  );
}

export default App;
