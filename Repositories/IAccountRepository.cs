using System.Collections.Generic;
using System.Threading.Tasks;

public interface IAccountRepository
{
    Task<Accounts> GetAccountByIdAsync(int id);
    Task<IEnumerable<Accounts>> GetAllAccountsAsync();
    Task AddAccountAsync(Accounts account);
    Task UpdateAccountAsync(Accounts account);
    Task DeleteAccountAsync(int id);
}
