import {
  QueryClient,
  QueryClientProvider,
  useQuery,
} from "@tanstack/react-query";
import { DefaultApiFactory } from "./api";
const queryClient = new QueryClient();

const BookList = () => {
  const api = DefaultApiFactory({
    basePath: "http://localhost:8000",
    isJsonMime: (mime: string) => mime === "application/json",
  });

  // Queries
  const query = useQuery({ queryKey: ["books"], queryFn: api.getBooks });
  return (
    <ul>
      {query.data?.data.map((book) => (
        <li key={book.id}>{book.title}</li>
      ))}
    </ul>
  );
};

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <BookList />
    </QueryClientProvider>
  );
}

export default App;
