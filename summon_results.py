import pygame


def summon_results(screen, cur):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
        results = cur.execute('''SELECT * FROM results order by level desc, last_score desc;''').fetchmany(5)
        for i in range(len(results)):
            font = pygame.font.Font(None, 75)
            string_rendered = font.render(
                f'name: {results[i][1].strip()}  level: {results[i][2]}  score: {results[i][3]}',
                                          1, pygame.Color('white'))
            text_rect = string_rendered.get_rect()
            text_rect.topleft = (100, 200 + 80 * i)
            screen.blit(string_rendered, text_rect)

        pygame.display.flip()
