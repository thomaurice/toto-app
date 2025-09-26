import { useQuery } from "@tanstack/react-query";
import { useParams, Link } from "react-router-dom";
import { useApi } from "../api/useApi";

export default function BookDetail() {
  const { bookId } = useParams<{ bookId: string }>();
  const api = useApi();

  const bookQuery = useQuery({
    queryKey: ["books", bookId],
    queryFn: () => api.getBook(Number(bookId)),
    enabled: !!bookId,
  });

  const bookContentQuery = useQuery({
    queryKey: ["book", bookId],
    queryFn: () => api.getBookContent(Number(bookId)),
    enabled: !!bookId,
  });

  const currentBook = bookQuery.data?.data;

  if (bookQuery.isLoading || bookContentQuery.isLoading) {
    return (
      <div>
        <div>Loading...</div>
      </div>
    );
  }

  if (bookQuery.isError || bookContentQuery.isError) {
    return (
      <div>
        <div>Error loading book details</div>
        <Link to="/">← Back to Books</Link>
      </div>
    );
  }

  if (!currentBook) {
    return (
      <div>
        <div>Book not found</div>
        <Link to="/">← Back to Books</Link>
      </div>
    );
  }

  return (
    <>
      <title>{currentBook.title}</title>
      <div>
        <div>
          <Link to="/">← Back to Books</Link>
        </div>
        <h1>{currentBook.title}</h1>
        <div className="whitespace-pre-wrap">
          {bookContentQuery.data?.data || "No content available"}
        </div>
      </div>
    </>
  );
}
