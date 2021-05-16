import "./GlobalStyle.css";
import "./App.css";
import { FiPlus, FiMinus } from "react-icons/fi";
import { FormEvent, useState } from "react";
import { api } from "./services/api";
import { toast } from "react-toastify";

type GameState = {
  name: string;
  categories: string;
  genres: string;
  steamspy_tags: string;
  positive_ratings: number;
  negative_ratings: number;
};

export function App() {
  const [searchGame, setSearchGame] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [games, setGames] = useState<GameState[]>([]);

  async function handleSubmit(event: FormEvent) {
    event.preventDefault();

    if (isLoading) {
      return;
    }

    if (!searchGame) {
      return;
    }

    setIsLoading(true);

    if (games[0]?.name) {
      setGames([]);
    }

    const response = await api.get("games", {
      params: {
        gameName: searchGame,
      },
    });

    if (response.data.data.games === "Jogo nao encontrado") {
      toast.error("Jogo não encontrado");
      setIsLoading(false);
      return;
    }

    setGames(response.data.data.games);

    setIsLoading(false);
  }

  return (
    <div className="container">
      <form className="form" onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Digite o nome do jogo"
          value={searchGame}
          onChange={(e) => setSearchGame(e.target.value)}
        />

        {isLoading ? (
          <button type="submit" style={{ cursor: "not-allowed" }}>
            Carregando ...
          </button>
        ) : (
          <button type="submit">Pesquisar</button>
        )}
      </form>

      {!isLoading && !!games[0]?.name ? (
        <div className="list-games">
          <table>
            <thead>
              <tr>
                <th>NOME</th>
                <th>CATEGORIAS</th>
                <th>GENEROS</th>
                <th>TAGS</th>
                <th className="plus-icon">
                  <FiPlus size={25} color="#43ff32" />
                </th>
                <th className="minus-icon">
                  <FiMinus size={25} color="#ff3600" />
                </th>
              </tr>
            </thead>
            <tbody>
              {games.map((game) => {
                return (
                  <tr key={game.name}>
                    <td>{game.name}</td>
                    <td>{game.categories}</td>
                    <td>{game.genres}</td>
                    <td>{game.steamspy_tags}</td>
                    <td>{game.positive_ratings}</td>
                    <td>{game.negative_ratings}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      ) : (
        isLoading && (
          <strong
            style={{ color: "white", marginTop: "10rem", fontSize: "2.4rem" }}
          >
            Carregando ...
          </strong>
        )
      )}
    </div>
  );
}
