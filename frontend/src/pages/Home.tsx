import { useQuery } from "@tanstack/react-query";
import { useApi } from "../api/useApi";

const BookList = () => {
  const api = useApi();
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
