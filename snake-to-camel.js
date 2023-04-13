function snakeToCamel(phrase) {
  const filter = [...phrase].map((letter, index) =>
    phrase[index - 1] == "_" ? letter.toUpperCase() : letter
  );
  const camel = filter.filter((letter) => letter != "_");
  return camel.join("");
}
