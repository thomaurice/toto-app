import { useQuery } from "@tanstack/react-query";
import { DefaultApiFactory } from "../api";

const api = DefaultApiFactory(
  {
    isJsonMime: (mime: string) => mime === "application/json",
  },
  "http://localhost:8000"
);

const BookList = () => {
  const query = useQuery({ queryKey: ["books"], queryFn: api.getBooks });
  return (
    <ul>
      {query.data?.data.map((book) => (
        <li key={book.id}>{book.title}</li>
      ))}
    </ul>
  );
};

export default function Home() {
  return (
    <>
      <title>Books</title>
      <div>
        <h1>Books</h1>
        <BookList />
      </div>
    </>
  );
}
